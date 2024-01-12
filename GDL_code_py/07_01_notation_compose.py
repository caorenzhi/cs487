#!/usr/bin/env python
# coding: utf-8

# In[2]:



from music21 import converter, chord, note


# # Getting the data
# 
# You can find midi files for each of the 36 movements in the J.S. Bach Cello Suites here:
# 
# http://www.jsbach.net/midi/midi_solo_cello.html
# 
# Save these inside the './data/cello' folder

# # Musical notation software
# 
# You'll also need to download some software to view and listen to the music generated by the model.
# 
# Musescore can be freely downloaded here:
# 
# https://musescore.org/en

# # Viewing the data

# In[9]:


dataset_name = 'cello'
filename = 'cs1-2all'
file = "./data/{}/{}.mid".format(dataset_name, filename)

original_score = converter.parse(file).chordify()


# In[10]:


original_score.show()


# In[3]:


original_score.show('text')


# # Extracting the data

# In[15]:


notes = []
durations = []

for element in original_score.flat:
    
    if isinstance(element, chord.Chord):
        notes.append('.'.join(n.nameWithOctave for n in element.pitches))
        durations.append(element.duration.quarterLength)

    if isinstance(element, note.Note):
        if element.isRest:
            notes.append(str(element.name))
            durations.append(element.duration.quarterLength)
        else:
            notes.append(str(element.nameWithOctave))
            durations.append(element.duration.quarterLength)

    


# In[25]:


print('\nduration', 'pitch')
for n,d in zip(notes,durations):
    print(d, '\t', n)


# In[ ]:



