import logging
import os
from nicegui import app, ui
from ezlab.parameters import DF, UA

from ezlab.pages import df, ua
from ezlab.utils import find_app

logger = logging.getLogger("ezlab.ui.ezmeral")


@ui.refreshable
def menu():

    disable_ua = True
    ezfabricctl_cmd = find_app("ezfabricctl")
    kubectl_cmd = find_app("kubectl")
    if ezfabricctl_cmd is not None and kubectl_cmd is not None and os.path.isfile("./ezfab-release.tgz"):
        disable_ua = False
        if not os.path.isdir("./.ezlab"):
            logger.info("Creating ./.ezlab folder for UA files")
            os.mkdir("./.ezlab")
    else:
        # TODO: offer the option to download the files
        logger.warning("Ezfabric files (kubectl, ezfabricctl and ./ezfab-release.tgz) not found, disabling UA !")

    with (
        ui.expansion(
            "Ezmeral",
            icon="analytics",
            caption="install, configure and use",
        )
        .classes("w-full")
        .classes("text-bold") as ezmeral
    ):

        with ui.tabs().classes("w-full") as tabs:
            one = ui.tab(DF)
            if not disable_ua:
                two = ui.tab(UA)
        with ui.tab_panels(tabs, value=one).classes("w-full"):
            # Data Fabric Workflow
            with ui.tab_panel(one):
                with ui.stepper().props("vertical header-nav").classes("w-full") as dfstepper:
                    with ui.step("Prepare", icon=""):
                        df.prepare_menu()
                        with ui.stepper_navigation():
                            ui.button(
                                "Run",
                                icon="play_arrow",
                                on_click=lambda: df.prepare_action(),
                            ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)
                            ui.button(
                                "Next",
                                icon="fast_forward",
                                on_click=dfstepper.next,
                            ).props("color=secondary")

                    with ui.step("Install"):
                        ui.input("Cluster Name", placeholder="ezlab").bind_value(app.storage.general[DF], "cluster_name").classes("w-full")

                        maprclusterhosts = (
                            ui.input(
                                "Hosts",
                                placeholder="One or more comma-separated IPs, i.e., 10.1.1.x,10.1.1.y",
                            )
                            .classes("w-full")
                            .bind_value(app.storage.general[DF], "maprclusterhosts")
                        )

                        ui.input(
                            "Data Disk(s)",
                            placeholder="One or more comma-separated raw disk path, i.e., /dev/sdb,/dev/vdb",
                        ).bind_value(
                            app.storage.general[DF], "maprdisks"
                        ).classes("w-full")

                        with ui.stepper_navigation():
                            ui.button(
                                "Run",
                                icon="play_arrow",
                                on_click=lambda: df.install_action(maprclusterhosts.value),
                            ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)
                            ui.button(
                                "Next",
                                icon="fast_forward",
                                on_click=dfstepper.next,
                            ).props("color=secondary")
                            ui.button("Back", icon="fast_rewind", on_click=dfstepper.previous).props("flat")

                    with ui.step("Cross-Cluster"):
                        ui.label("Configure cross cluster communication between two clusters")
                        ui.input("Local Cluster CLDB node", placeholder="core.ez.lab").bind_value(app.storage.general[DF], "crosslocalcldb").classes(
                            "w-full"
                        )
                        ui.input("Remote Cluster CLDB node", placeholder="edge.ez.lab").bind_value(
                            app.storage.general[DF], "crossremotecldb"
                        ).classes("w-full")
                        ui.input("Cluster Admin User", placeholder="mapr").bind_value(app.storage.general[DF], "crossadminuser").classes("w-full")
                        ui.input(
                            "Cluster Admin Password",
                            placeholder="mapr",
                            password=True,
                            password_toggle_button=True,
                        ).bind_value(
                            app.storage.general[DF], "crossadminpassword"
                        ).classes("w-full")

                        with ui.stepper_navigation():
                            ui.button(
                                "Run",
                                icon="play_arrow",
                                on_click=lambda: df.xcluster_action(),
                            ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)
                            ui.button(
                                "Next",
                                icon="fast_forward",
                                on_click=dfstepper.next,
                            ).props("color=secondary")
                            ui.button("Back", icon="fast_rewind", on_click=dfstepper.previous).props("flat")

                    with ui.step("Client"):
                        ui.label("Setup a client to a Data Fabric cluster")
                        ui.input("Server", placeholder="Hostname or ip address").bind_value(app.storage.general[DF], "connect_to")
                        ui.switch("Remote", value=False).bind_value(app.storage.general[DF], "isclientremote")
                        ui.input("Client", placeholder="Hostname or ip address").bind_value(
                            app.storage.general[DF], "maprclient"
                        ).bind_visibility_from(app.storage.general[DF], "isclientremote")
                        with ui.stepper_navigation():
                            ui.button(
                                "Run",
                                icon="play_arrow",
                                on_click=lambda: df.client_action(),
                            ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)
                            ui.button("Back", icon="fast_rewind", on_click=dfstepper.previous).props("flat")

            if not disable_ua:
                # so we can serve kubeconfig files
                app.add_static_files("/files", ".ezlab")

                # Unified Analytics Workflow
                with ui.tab_panel(two):
                    with ui.stepper().props("vertical header-nav").classes("w-full") as uastepper:
                        with ui.step("Prepare", icon=""):

                            ui.input("Cluster Name", placeholder="ezlab").bind_value(app.storage.general[UA], "clustername").classes("w-full")

                            ui.input("Orchestrator", placeholder="10.1.1.11").bind_value(app.storage.general[UA], "orchestrator").classes("w-full")
                            ui.input("K8s Master", placeholder="10.1.1.12").bind_value(app.storage.general[UA], "controller").classes("w-full")
                            ui.input("Workers", placeholder="10.1.1.13,10.1.1.14,10.1.1.15").bind_value(app.storage.general[UA], "workers").classes(
                                "w-full"
                            )

                            with ui.stepper_navigation():
                                ui.button(
                                    "Run all!",
                                    icon="play_arrow",
                                    on_click=ua.runall_action,
                                ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)
                                ui.button(
                                    "Run",
                                    icon="play_arrow",
                                    on_click=ua.prepare_action,
                                ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)
                                ui.button(
                                    "Next",
                                    icon="fast_forward",
                                    on_click=uastepper.next,
                                ).props("color=secondary")

                        with ui.step("Prechecks", icon=""):

                            with ui.row():
                                ui.label(f"Orchestrator:")
                                ui.label().bind_text_from(app.storage.general[UA], "orchestrator")

                            with ui.row():
                                ui.label(f"Controller:")
                                ui.label().bind_text_from(app.storage.general[UA], "controller")

                            with ui.row():
                                ui.label(f"Workers:")
                                ui.label().bind_text_from(app.storage.general[UA], "workers")

                            with ui.stepper_navigation():
                                ui.button(
                                    "Run",
                                    icon="play_arrow",
                                    on_click=ua.precheck_action,
                                ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)
                                ui.button(
                                    "Next",
                                    icon="fast_forward",
                                    on_click=uastepper.next,
                                ).props("color=secondary")

                        with ui.step("Install", icon=""):

                            with ui.row():
                                ui.label(f"Orchestrator:")
                                ui.label().bind_text_from(app.storage.general[UA], "orchestrator")

                            with ui.row():
                                ui.label(f"Controller:")
                                ui.label().bind_text_from(app.storage.general[UA], "controller")

                            with ui.row():
                                ui.label(f"Workers:")
                                ui.label().bind_text_from(app.storage.general[UA], "workers")

                            with ui.stepper_navigation():
                                ui.button(
                                    "Run",
                                    icon="play_arrow",
                                    on_click=ua.install_action,
                                ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)
                                ui.button(
                                    "Next",
                                    icon="fast_forward",
                                    on_click=uastepper.next,
                                ).props("color=secondary")

                        with ui.step("Deploy", icon=""):

                            with ui.row():
                                ui.label(f"Orchestrator:")
                                ui.label().bind_text_from(app.storage.general[UA], "orchestrator")

                            with ui.row():
                                ui.label(f"Controller:")
                                ui.label().bind_text_from(app.storage.general[UA], "controller")

                            with ui.row():
                                ui.label(f"Workers:")
                                ui.label().bind_text_from(app.storage.general[UA], "workers")

                            with ui.stepper_navigation():
                                ui.button(
                                    "Run",
                                    icon="play_arrow",
                                    on_click=ua.deploy_action,
                                ).bind_enabled_from(app.storage.user, "busy", backward=lambda x: not x)

    ezmeral.bind_value(app.storage.general["ui"], "ezmeral")
