"""Test file so I can run quick snippet inside unreal"""
import os
import opentimelineio as otio
#import path_utils
import unreal


def export_sequencer_data_as_otio():
    """Export out of unreal folder"""
    # Get the output folder for the out usd data
    out_dir = '/home/dimitri/dev/'
    print(os.path.exists(out_dir))
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    timeline = otio.schema.Timeline(name="MyTimeline")
    track = otio.schema.Track()
    timeline.tracks.append(track)

    out_path = out_dir + "my_timeline.otio"

    unreal.log("yay")
    unreal.log(out_dir)

    print(timeline)
    if os.path.exists(out_dir):
        print("path exists!")
        otio.adapters.write_to_file(timeline, out_path)
    else:
        unreal.log_error("Can't write OTIO files, {} dir does not exists".format(out_dir))



export_sequencer_data_as_otio()