### Hexlet tests and linter status:
[![Actions Status](https://github.com/Semeikin-Kirill/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Semeikin-Kirill/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3671276004864a1ddc26/maintainability)](https://codeclimate.com/github/Semeikin-Kirill/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3671276004864a1ddc26/test_coverage)](https://codeclimate.com/github/Semeikin-Kirill/python-project-50/test_coverage)

## Difference calculator

### Setup

```
$ make install
```

### Comparison of flat files (JSON)

```
$ gendiff <filepath1> <filepath2>
```

[![asciicast](https://asciinema.org/a/pEWUDEcmTkzrFEjQw3j3OOtxG.svg)](https://asciinema.org/a/pEWUDEcmTkzrFEjQw3j3OOtxG)

### Comparison of flat files (YAML)

```
$ gendiff <filepath1> <filepath2>
```

[![asciicast](https://asciinema.org/a/tATx8ZBpejM30acmHZtl0SBV6.svg)](https://asciinema.org/a/tATx8ZBpejM30acmHZtl0SBV6)

### Nested structure comparison (JSON and YAML)

[![asciicast](https://asciinema.org/a/iWpDbiI1ZvQv8NZaUVuJXGLIH.svg)](https://asciinema.org/a/iWpDbiI1ZvQv8NZaUVuJXGLIH)

### Flat format

```
$ gendiff --format plain <filepath1> <filepath2>
```

[![asciicast](https://asciinema.org/a/E3BWuuJR4nkEpZ8Cg3kIMhIor.svg)](https://asciinema.org/a/E3BWuuJR4nkEpZ8Cg3kIMhIor)

### Get the differences in json format

```
$ gendiff -- format json <filepath1> <filepath2>
```

[![asciicast](https://asciinema.org/a/wyC0TMDSunJckdaaJKsgwlcjC.svg)](https://asciinema.org/a/wyC0TMDSunJckdaaJKsgwlcjC)
