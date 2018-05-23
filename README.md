# Image resizer

It change an image to several different sizes.
## Input settings

```json
{ "input" : "input.png" }
```

Enter the name of the original image file in the value of input.


## Output settings


```json
{
  "output":
  [
  {"size":[144,144], "filename":"android-icon-{x}x{y}.png", "type":"png"},
  {"size":[192,192], "filename":"android-icon-{x}x{y}.png", "type":"png"}
  ]
}
```

The configuration can be done in json format and you can enter the desired output information in the value of list.
__{X}__ in Filename is replaced with index number 0 in the size list, and __{y}__ is replaced with index number 1.

The resized image is stored in the _result_ directory.
