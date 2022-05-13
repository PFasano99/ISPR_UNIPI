# Intelligent Systems for Pattern Recognition 2021/2022

## Introduction
The following repo contains the midterms for the course of Intelligent Systems for Pattern Recognition 2021/2022 of the master's degree in artificial intelligence from the University of Pisa.  
The course introduces students to the analysis and design of advanced machine learning and deep learning models for modern pattern recognition problems and discusses how to realize advanced applications exploiting computational intelligence techniques.
The different midterms assigned during the course are developed in notebooks and most of the "design" choices are commented; each midterm is centered on a different topic.   
The topics are listed below:

<br>

### Midterm 1
The musical pitch of a note is determined by its fundamental frequency. The pitch played by different instruments sounds different due to harmonics, i.e. other frequencies that are superimposed and determine the timbre of the instrument. <a href="https://philharmonia.co.uk/resources/sound-samples/"> This dataset</a> contains samples from several instruments playing different notes. Plot the spectrogram for some of them (4 instruments are sufficient) and check if it is possible to recognize the different instruments by only looking at the spectrogram. In your presentation, discuss which samples you chose to compare, how you computed the spectrogram and whether the resulting features are sufficient to recognize the instrument.  

In Python you can import WAVs (and acces several other music-related functions), using the LibROSA library.

<br>

### Midterm 2
Implement a simple image understanding application for DSET2 using the LDA model and the bag of visual terms approach. For details on how to implement the approach see the BOW demo and paper <a href="https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/csurka-eccv-04.pdf">[G. Csurka, C. R. Dance, L. Fan, J. Willamowski, and C. Bray. Visual Categorization with Bags of Keypoints. Workshop on Statistical Learning in Computer Vision. ECCV 2004]</a>.  Keep one picture for each image subset (identified by the initial digit in the filename) out of training for testing. In short:

1. For each image (train and test) extract the SIFT descriptors for the interest points identified by the MSER detector.

2. Learn a 500-dimensional codebook (i.e. run k-means with k=500 clusters) from  the SIFT descriptors of the training images (you can choose a subsample of them if k-means takes too long).

3. Generate the bag of visual terms for each image (train and test): use the bag of terms for the training images to train an LDA model (use one of the available implementations). Choose the number of topics as you wish (but reasonably).

4. Test the trained LDA model on test images: plot (a selection of) them with overlaid visual patches coloured with different colours depending on the most likely topic predicted by LDA.

<a href="http://download.microsoft.com/download/A/1/1/A116CD80-5B79-407E-B5CE-3D5C6ED8B0D5/msrc_objcategimagedatabase_v1.zip"> DSET2 (Image processing):</a>

<br>

### Midterm 3
<a href="https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset">DATASET (Fake News Classification) - Dataset</a>

The dataset contains real and fake news, including their title, text, subject, and date. The objective is to train a binary classifier to recognize fake news. You are free to choose the model's architecture, but you should describe and justify your design choices.

Notice that the fake and real news in the dataset are balanced. However, in the real world, real news are much more frequent than fake ones (hopefully). Simulate the effect of the data imbalance by undersampling/oversampling one of the classes in the training set and compute the test accuracy on a (balanced) test set. Then, try to use a mechanism to make the training robust to imbalances, such as weighting the loss for the samples depending on their class. Discuss the results of this mitigation.

---

## Contact information

If you have any problems to install this repository or need any clarification on the code please contact us at: 

|Author             |University Mail                    | Personal Mail             | Github                                                   |
|-------------------|-----------------------------------|---------------------------|----------------------------------------------------------|
| Paolo Fasano      | p.fasano1@studenti.unipi.it       | p.fasano99@hotmail.com    | <a href="https://github.com/PFasano99/">Paolo Fasano</a> |

