"""Init file that is used as unreal starts"""
import unreal
import export_usd
import export_sequencer


@unreal.uclass()
class ExportUsdScript(unreal.ToolMenuEntryScript):
    """Class to write exec script of a button"""
    @unreal.ufunction(override=True)
    def execute(self, context):
        unreal.log("Exporting USD data out of unreal")
        export_usd.export_usd_data_out_of_world()

@unreal.uclass()
class ExportSequencerToOtio(unreal.ToolMenuEntryScript):
    """Class to write exec script of a button"""
    @unreal.ufunction(override=True)
    def execute(self, context):
        #unreal.log("Not doing anything for now as import opentimelineio is making unreal crash.")
        unreal.log("Exporting Sequencer Data using OTIO")
        export_sequencer.export_sequencer_data_as_otio()

def create_usdexport_button():
    """Create USDExport button inside the editor"""
    menus = unreal.ToolMenus.get()
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    usd_export_menu = main_menu.add_sub_menu("Owner", "SectionName", "UsdExport", "Usd Export")

    # Export Usd button
    script_object = ExportUsdScript()
    script_object.init_entry(
        owner_name=usd_export_menu.menu_name,
        menu=usd_export_menu.menu_name,
        section="EditMain",
        name="UsdExport",
        label="Export Usd",
        tool_tip="Export Usd Data out of Unreal"
    )
    script_object.register_menu_entry()

    # Export sequencer button
    script_object = ExportSequencerToOtio()
    script_object.init_entry(
        owner_name=usd_export_menu.menu_name,
        menu=usd_export_menu.menu_name,
        section="EditMain",
        name="ExportSequencer",
        label="ExportSequencer",
        tool_tip="Export Sequencer Data as OTIO format"
    )
    script_object.register_menu_entry()

    menus.refresh_all_widgets()

def main():
    """Main method."""
    unreal.log("Executing main()")
    create_usdexport_button()

if __name__ == '__main__':
    main()
