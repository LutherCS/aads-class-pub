# Anomaly counter

Implement the *flood fill* algorithm to count number of anomalies in a picture.

Your program must count the number of anomalies (stars, spots, facial features etc) visible in a bitmap image.
An image consists of pixels, and each pixel is either black (represented by the characters `·`, `.`, or a space) or white (represented by `*`).
All black pixels are considered to be part of the background, and each white pixel is considered to be part of an anomaly.

An argumenbt `sides` must be passed to the function `count` to specify the adjacency rule.
If white pixels are adjacent vertically or horizontally only, `sides` is equal to 4.
If diagonally adjacent pixels are considered part of the same anomaly, `sides` is equal to 8.

Each data file in *data/projects/anomalycounter/* represents a single image as rows and columns of pixels.

For each test case, count the number of anomalies in the image.

## Testing

Run the application as follows:

```bash
python src/projects/anomalycounter/anomalycounter.py --sides 4
python src/projects/anomalycounter/anomalycounter.py --sides 8
```

Use the provided unit tests:

```bash
python -m pytest tests/projects/anomalycounter/
```

## References

- [ASCII Art Smileys - asciiart.eu](https://www.asciiart.eu/computers/smileys)
