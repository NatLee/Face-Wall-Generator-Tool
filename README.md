# Face Wall Generator Tool

This is a tool for generating face wall to verify some AI models.

## Usage

`python3 main.py -x <COLUMN> -y <ROW> -save_path <YOUR_SAVE_PATH>`

> Please put you faces into folder `./faces`.

If `-save_path` is null, it will save `./wall.jpg` as default.

## Help

`python3 main.py --help`

```
NAME
    main.py - Generate wall!

SYNOPSIS
    main.py X Y SAVE_PATH

DESCRIPTION
    Generate wall!

POSITIONAL ARGUMENTS
    X
        Type: int
    Y
        Type: int
    save_path(optional)
        Type: str
```

## Sample

![sample](./docs/sample.png)