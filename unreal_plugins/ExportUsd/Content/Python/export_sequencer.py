"""Module to export sequencer data using OTIO"""
import os
import opentimelineio as otio
import path_utils
import unreal


def get_master_sequencer():
    """Get the master sequencer in the content browser."""

    #/Game/ represents the root of the Content folder
    path = "/Game/MasterSequencer.MasterSequencer"
    master_sequencer = unreal.EditorAssetLibrary.load_asset(path)

    if master_sequencer:
        return master_sequencer
    else:
        unreal.log_error("Could not find 'MasterSequencer' LevelSequencer in the Content folder")
        return None

def export_sequencer_data_as_otio():
    """Export out of unreal folder"""
    # Get the output folder for the out usd data
    out_dir = path_utils.get_otio_export_folder()
    master_sequencer = get_master_sequencer()
    print(os.path.exists(out_dir))
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Find shot track
    master_shot_track = master_sequencer.find_tracks_by_exact_type(unreal.MovieSceneCinematicShotTrack)[0]

    if out_dir and master_sequencer:
        unreal.log("yay")
        unreal.log(out_dir)
        unreal.log(master_sequencer)
        # Creat OTIO timeline
        timeline = otio.schema.Timeline(name="MyTimeline")
        track = otio.schema.Track()
        timeline.tracks.append(track)

        # Get shots inside the master sequence adn add them to the timeline
        for shot in master_shot_track.get_sections():
            shot_name = shot.get_shot_display_name()
            start_frame = shot.get_start_frame()
            end_frame = shot.get_end_frame()

            clip = otio.schema.Clip(name=shot_name)
            duration = end_frame - start_frame + 1

            clip.source_range = otio.opentime.TimeRange(
                start_time=otio.opentime.RationalTime(start_frame, 24),  # Assuming 24 fps
                duration=otio.opentime.RationalTime(duration, 24)
            )
            track.append(clip)
        
        # out_path = out_dir + "my_timeline.otio"

        unreal.log("yay")
        unreal.log(out_dir)

        # print(timeline)
        if os.path.exists(out_dir):
            print("eheheh")
            #otio.adapters.write_to_file(timeline, out_path)
        else:
            unreal.log_error("Can't write OTIO files, {} dir does not exists".format(out_dir))

    else:
        unreal.log_error("Interrupting sequencer data export.")


# export_sequencer_data_as_otio()