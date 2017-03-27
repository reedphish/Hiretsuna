# Hiretsuna

## About

Hiretsuna is a project initalized by Reedphish Heavy Industries (RHI) for malware research purposed.
The name Hiretsuna itself is Japanese and means ___sneaky___. 

## Prerequisites

* Python 2.7.x (Python 3 may work)
* PIL

## Usage

For now there are two scripts available. One for embedding "secret" text in image hidden in RGB values
of the first "column" and one script for decoding. Both has been testen on PNG's.

### Encode image

```bash
$ python encode-image.py arg_1 arg_2 arg_3
```

| Arg. position | Desciption                       | Example                       |
| :------------ | :------------------------------- | :---------------------------- |
| 1             | Path to text to include in image | example_texts/Short_poem.txt  |
| 2             | Path to original image           | base_images/psychedelic-1.png |
| 3             | Path to output image             | example_images/testimage.png  |

Script will output a key that you can use to decode this image.

#### Example
```bash
$ python encode-image.py example_texts/Short_poem.txt base_images/psychedelic-1.png example_images/testimage.png
```

### Decode image

```bash
$python decode-image.py arg_1 arg_2 arg_3
```

| Arg. position | Desciption                      | Example                       |
| :------------ | :------------------------------ | :---------------------------- |
| 1             | Where to write the decoded text | decoded.txt                   |
| 2             | Path to encoded image           | base_images/psychedelic-1.png |
| 3             | Key to unlock the message       | example_images/testimage.png  |


#### Example
```bash
$python decode-image.py decoded.txt example_images/testimage.png 55
```