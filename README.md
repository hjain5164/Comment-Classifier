# Toxic-Comment-Classification

![](https://github.com/piyushmanglani08/TEKSystems_HACK/blob/master/Image.jpeg)

### Project Description:

With the recent growth of people on the internet, civil conversations are seeing a decline. “Whatever intelligent observations do lurk there are often drowned out by obscenities, ad-hominem attacks, and off-topic rants.” These things are forcing many online platforms which once flourished with intellectual discussions to close the comment sections. To facilitate meaningful conversations on their online platform The New York Times employed full-time moderators who moderate nearly 11,000 comments per day on the selected article(roughly 10% of Times articles). However, for small firms operating people for these tasks might be out of scope. To aid, the Conversation AI team, a research initiative founded by Jigsaw and Google (both a part of Alphabet) are working on tools to help improve online conversation. One area of focus is the study of negative online behaviors, like toxic comments (i.e. comments that are rude, disrespectful or otherwise likely to make someone leave a discussion). So far they’ve built a range of publicly available models served through the Perspective API, including toxicity.

### Data

Source: It consists of large number of Wikipedia comments which have been labeled by human raters for toxic behavior. 
The types of toxicity are: 
- Anger 
- Joy
- Sadness 
- Shame 
- Guilt 
- Disgust
- Fear

###Pre_Requisite

   Python Version should be 3.7.0 or above.
   pip should be present.

###Steps to install Flask on your System

Type following commands on your terminal.

   pip install virtualenv using the command "sudo pip3 install virtualenv"
   Now create a virtual environment using "virtualenv venv" you can use any name insted of venv
   Move to project folder using cd command
   Run the command "pip install flask"

###How to execute the code on your System

   Open your terminal , move to project folder using cd command.
   Run python flask_2.py on terminal
   Wait for few seconds for model training.
   Move to the port http://127.0.0.1:5000/ which is being locally hosted.
   Bang !! Find out whether the comment is toxic or not
