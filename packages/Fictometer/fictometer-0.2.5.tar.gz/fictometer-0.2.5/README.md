# Fictometer

## Description

Fictometer is an algorithm for analysing whether the given text is ```Fiction``` or ```Non-Fiction```.
It first calculates the number of ```adverbs```, ```adjectives``` and ```pronouns``` in the text.
It then calculates Ratio of Adjective to Pronoun ```RADJPRON``` and Ratio of Adverb to Adjective ```RADVADJ```, 
from which it predicts whether text is ```Fiction``` or ```Non-Fiction```.

Blog Link: 🔗[LINK](https://bekushal.medium.com/fictometer-a-simple-and-explainable-algorithm-for-sentiment-analysis-31186d2a8c7e)


## Installation

```bash
pip install Fictometer
```


## Usage
```bash
import Fictometer

text = "your_text"

pc = Fictometer.counts(text)
// returs the count of ```adjectives```, ```adverbs``` and ```pronouns```

result = Fictometer.predict(text)
// Uses counts(), then calculates RADJPRON and RADVADJ, and returns a tuple having 'result' and 'confidence'.

Fictometer.help()
// Shows how to use the package
```


## Contact

email - atmabodha@gmail.com