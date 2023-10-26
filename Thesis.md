# Bachelor Thesis Design
## Exploring Reaction Time in an actual whole-body Jump’n Run Game
we develop a VR game in which players will respond to terrain changes simulated by smart shoes. We tested participants under different sound conditions
and observed their reaction times to terrain changes. We also performed simple
response tests on participants’ eye-hand reaction times to validate the results
of previous studies. Finally we find that most participants have a much slower
tactile response time to the foot than the eye-hand response. Moreover, the different sound conditions bring about a greater effect on the tactile response of
the foot than the eye-hand response.

## Experiment Tools
VR-HMD will be used for the demonstration of VR games. The game
is created and packaged into the head display through the unity engine, thanks
to the advantages of the meta quest pro all-in-one.

<div align="center">
    <img src="./assets/images/Meta quest pro.jpg" width="300px" display="inline"> 
    <div>
        <p>Meta quest pro</p>
    </div>
</div>

iPhone12 pro is really useful for its camera, as it is needed to record
the images of the subject during the experiment and to assist in determining the
reaction time data.

<div align="center">
    <img src="./assets/images/iphone12 pro.jpg" width="300px" display="inline"> 
    <div>
        <p>iPhone12</p>
    </div>
</div>

The air pods pro is used to create different sound environments for
the purpose of controlling variables.

<div align="center">
    <img src="./assets/images/airpods.jpg" width="300px" display="inline"> 
    <div>
        <p>Air pods pro</p>
    </div>
</div>

The smart insoles are useful in two ways. The first is the ability to
simulate changes in terrain, such as asphalt, grassy and sand. The second is
to capture the subject’s responses and record them via sensor transmission to a
computer terminal.

<div align="center">
    <img src="./assets/images/prototype.png" width="600px" display="inline"> 
    <div>
        <p>smart insoles</p>
    </div>
</div>


## Experiment Design
The experiment was divided into a simple reaction test and a VR scene reaction test.

### Simple Reaction Test
The experiment is conducted on the Human Benchmark website<a href="https://humanbenchmark.com" target="_blank">(https://humanbenchmark.com).</a> The experiment will be conducted five times
and the final results will be averaged. Participants will be tested under three different sound conditions while wearing headphones, and the experimenter will
record the results. The response speed of the participants is measured under
noise reduction, soothing background sound and high background sound as follows.

<div align="center">
    <img src="./assets/images/Eye-hand experiment data.png" width="600px" display="inline"> 
    <div>
        <p>Eye-hand experiment data</p>
    </div>
</div>

### VR Scene Reaction Test
Participants wear VR equipment and adjust the level of comfort and pupil distance to ensure they can clearly see the scene inside the helmet. Participants put
on the insoles, wear the headset, and start walking back and forth along the corridor after the experimenter sets up the phone and starts recording. Instructions
are given to the insoles via keystrokes on the computer, and the time it took for
the participant to respond is recorded. From the frame in the program when the
mouse is released to give the command, to the end of the frame when the subject gives the signal. The time in between will be used as the subject’s reaction
time to the simulated terrain change.

<div align="center">
    <img src="./assets/images/scene.png" width="800px" display="inline"> 
    <div>
        <p>VR scene</p>
    </div>
</div>

## Result
<div align="center">
    <img src="./assets/images/result.png" width="600px" display="inline"> 
    <div>
        <p>VR scene experiment data</p>
    </div>
</div>

The Number column is the serial number of the stimulus. There are four types,
Inflation, Deflation, Vibration on and Vibration off. The Sound column is the
sound played in the participant’s headphones, and there are three types: Quiet,
which is the noise-canceling environment; Soothing, which plays soothing music; and High, which plays high music. The Start column refers to the frame
where the stimulus start, that is, the frame where the experimenter released
the mouse. The Respond column refers to whether the participant respond to
the stimulus or not, the main purpose of this column is to calculate the error
rate. The Reaction column refers to the frame where the participant start to
respond. The RT column is calculated from the Start column and the Respond
column. Since the video is captured at 60 frames, the reaction time is given by
the following equation.

$$RT(ms)=(Reaction-Start)*1000(ms)/60$$

## Paper
More details please take a look at：<a href="./paper.pdf" target="_blank">Thesis Paper.</a>
