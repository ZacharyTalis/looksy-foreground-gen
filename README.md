# looksy-foreground-gen

A generator script for [Looksy](https://prodzpod.github.io/witness/editor.html) foreground images.

Only works for in-cell icons (no support for in-path icons).

Thanks to Mak for the foreground image size equation and to u-ndefined for the icon tinting implementation!

**[Google Colab version (runs in-browser)](https://colab.research.google.com/drive/1P9meW2hCtEZAgQxFuaYNTFlxUSzxduGE)**

## Run info

### Format

```shell
python3 main.py <icons> \[colors\] <x,y> <placements>
```

- **Icons**: Names of icons to be used, which can be found in `icons` folder. Each icon is separated by a comma `,`.
- **Colors**: Names of colors to be used, which can be found in the [Colors section](#colors). Each color is separated by a comma `,`. This is an optional argument.
- **x,y**: The panel's width and height, respectively.
- **Placements**: Syntax to place the icons:
  - A number specifies the index of icon to be used. The number `0` represents a blank icon.
  - The current cell is in the first row and column by default. The character `,` moves to the next column. `-` moves to the first column on the next row.
  - To specify an icon color, add a `c` and a color index just after the icon index.

### Paths

All icons should be PNGs and reside within the `icons` folder. Each output is saved to the `output` folder as `foreground.png`.

### Colors

Available predefined colors currently are:

- Looksy: (available by adding `looksy-` into the beginning, then specifying the color at the below table)

| Colors      | Colors        | Colors       |
| ----------- | ------------- | ------------ |
| `white`     | `black`       | `grey`       |
| `red`       | `pink`        | `darkred`    |
| `orange`    | `lightred`    | `orangered`  |
| `yellow`    | `lightyellow` | `gold`       |
| `darkgreen` | `green`       | `lightgreen` |
| `blue`      | `blueviolet`  | `lightcyan`  |
| `purple`    | `violet`      | `magenta`    |

- Other options are: `black`, `grey`, `white`, `darkred`, `red`, `orange`, `olive`, `yellow`, `darkgreen`, `green`, `teal`, `cyan`, `darkblue`, `blue`, `purple`, and `magenta`.
- The program supports hexadecimal color values (three-digit and six-digit), with `+` substituting for the standard `#`. For example, `+08f` and its equivalent `+0088ff`.
- There is also the RGB format `red-green-blue`, where each channel has a range between 0 to 255 inclusively (e.g. `0-140-255`).

### Examples

Generate a 2x4 foreground image with row order `blanks -> stars -> hearts -> blanks`:

```shell
python3 main.py star,heart 2,4 0,0-1,1-2,2
```

Generate a 3x3 foreground image with hearts placed diagonally. Each row is colored in red, then green, then blue:

```shell
python3 main.py heart looksy-red,looksy-green,looksy-blue 3,3 0,0,1c1-0,1c2,0-1c3
```
