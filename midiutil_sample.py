# ------------------------------------------------------------------------------
	# Creates a super-simple midi file.
	# requires some way of playing MIDIs, such as FluidSynth, and a Sound Font
	# note that the generated file seems very quiet
# ------------------------------------------------------------------------------

#Import the library
from midiutil.MidiFile import MIDIFile
 
# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.
track = 0   
time = 0
 
# Add track name and tempo.
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time,120)

# Add a note. addNote expects the following information:
track = 0
channel = 0
pitch = 60
timer = 0
duration = 1
volume = 255  # max 255
 

# Now add the note.
MyMIDI.addNote(track,channel,pitch,time,duration,volume)

for timer in xrange(10):
	MyMIDI.addNote(track,channel,pitch+(timer),timer,duration,volume)
	MyMIDI.addNote(track,channel,pitch+(2*timer),timer,duration,volume)
	MyMIDI.addNote(track,channel,pitch-(2*timer),timer,duration,volume)


# And write it to disk.
binfile = open("sample_output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

# if __name__ == "__main__":
