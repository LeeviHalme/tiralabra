# Testing

The app is tested in various ways. The most important tests are the unit tests that are run with pytest. The unit tests are located in the `tests` folder. The unit tests are run automatically with GitHub Actions on every push. The test coverage is also calculated automatically and uploaded to Codecov. The Codecov project can be found [here](https://codecov.io/gh/LeeviHalme/tiralabra).

## Running the tests

The tests can be run with the following command:

```bash
poetry run poe test
```

## Unit tests and branch coverage

All data structures and algorithms are tested with unit tests. Branch coverage percent can be found from the project's README file.

Coverage graph can be found below:

![Branch coverage](https://codecov.io/gh/LeeviHalme/tiralabra/graphs/tree.svg?token=296GA4LY45)

_Each block represents a single file in the project. The size and color of each block is represented by the number of statements and the coverage, respectively._

## Algorithm testing

_To be added_
