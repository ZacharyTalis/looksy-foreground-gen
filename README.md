# looksy-foreground-gen

A generator script for [Looksy](https://prodzpod.github.io/witness/editor.html) foreground images.

Only works for in-cell icons (no support for in-path icons).

Thanks to Mak for the foreground image size equation!

## Run info

### Format
```shell
python3 main.py <x,y> <icons> <placements>
```

### Example
To generate a 2x4 foreground image with row order `blanks -> stars -> hearts -> blanks`
```shell
python3 main.py star,heart 2,4 0,0-1,1-2,2
```

### Paths
All icons should be PNGs and reside within the `icons` folder. Each output is saved to the `output` folder as `foreground.png`.