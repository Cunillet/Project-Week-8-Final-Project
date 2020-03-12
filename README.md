<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Animals live detector
*Oriol Cunill Fulquet*

*Data Analytics, 2020/03/11 - IronHach - Barcelona*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
Every day we use deep learning algorithms and don't even think about it. Just think about the errors but don't put attention on how good they do it. In this project my only goal is to understand and try to reproduce something that already exists: a classificator of images, in this case, animals.

## Hypotheses / Questions
* Is it possible to reproduce an image classificator in one week without knowledge in deep learning?
* Is there any difference between processing stored images and live cam recognition?
* Are chosen species determinant for this experiment? Also, more classifications affect the results?

## Dataset
* the main dataset is from [Kaggle](https://www.kaggle.com/alessiocorrado99/animals10), a dataset with ten animals, more than 1000 images per animal.
* After doing this process, I would say that, 1000 images, when trying to classify 10 different animals, is not enough, specialy when some animals have different races.

## Cleaning
As long as my data were just images my first thought was I wouldn't need to clean. Truth is I found algorithms not working propperly and that was because there were wrong images or confusing images. This made me clean (at least the worse) images manualy for training and testing.

## Model Training and Evaluation
Searched and did fast tests with two deep learning libraries: [Tensorflow](https://www.tensorflow.org/) and [Pytorch](https://pytorch.org/). Decided to go for Tensorflow because found more documentation and seemed to be a bit faster to understand and learn.
Once the library was chosen, next step is to decide the layers. First tests were done with [Dense](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense). This layer search for a full pattern, this was a mistake because the objective is not tot detect a full image but part of its content. The right layer is one specialised in images or in searching patterns inside a whole. I decided to go for [Conv2D](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D). This layer is specialised in searching elements in a whole. Another problem to take care of is, images have two dimensions and the output was a list of ten elements so before processing the result [Flatten](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten) was needed.
When a library is decided and layers are chosen, just one thing is pending; decide how many and how to play with them, parameters, etc.

## Conclusion
* Deep learning is harder than thought, there isn't a math calculation to be sure of how many loops, how many layers, how many nodes per layer, etc. You end up figuring out what works better by intuition but can't explain that intuition as well as I would like
* There is a big difference when processing images stored and with live camera processing. As long as is image processing, my first though was there would be no difference but after working with it, found that some classes that can't be well processed in images are well processed in live and oposite. Also hard to find the balance of well processing each class.

## Future Work
This project still needs a lot of work. Specially with squirtles, the best saved model has a problem with two animals and still need to improve the live processing.

## Workflow
1. check different parameters
2. with correct parameters, check different number of layers and different number of deepness
3. look for the "best" number of loops for the previos decided points
4. test with new images
5. test in live cam

## Links
[Animal live detector](https://github.com/Cunillet/Project-Week-8-Final-Project)
[Slides](https://docs.google.com/presentation/d/1uO_FQ-t5czcJEXMGsVuMUooYMo7ZAIZRr6pyikVJOC4/edit#slide=id.p)
[Trello](https://trello.com/en)
