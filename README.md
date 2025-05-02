# nude-split
**nude-split** is an intelligent sorting tool that automatically separates your spicy content from your safe-for-work media — so you don’t have to.
Powered by machine learning, it scans your photo library and cleanly splits nudes from non-nudes, preventing awkward surprises in your gallery or camera roll.

Keep your secrets safe, and your scrolls workplace-friendly.
---
## How It Works
nude-split uses a nudity detection algorithm based on the paper:
[An Algorithm for Nudity Detection by R. Ap-Apid](https://www.researchgate.net/publication/249767252_An_Algorithm_for_Nudity_Detection), presented at PCSC 2005.

The algorithm identifies nudity in color images by:

Modeling skin color distributions using color spaces.

Detecting and segmenting skin regions within an image.

Analyzing the shape, size, and distribution of these regions for patterns indicative of nudity.

With a reported detection accuracy of 94.77%, the model is both fast and impressively reliable.
---
## 🔐 Why nude-split?
**Private**: Runs locally — your images never leave your device.

**Accurate**: Built on a proven algorithm for real-world performance.

**Helpful**: No more blending your nudes with your vacation photos.
---

Want a clean gallery and peace of mind? Let nude-split do the dirty work.

Requirements
Python2.7+ and Python3.3+
Cython
Pillow

Usage via command-line
``` bash
$ nudepy IMAGE_FILE
```
via Python Module
``` python 
import nude
from nude import Nude

print(nude.is_nude('./nude.rb/spec/images/damita.jpg'))

n = Nude('./nude.rb/spec/images/damita.jpg')
n.parse()
print("damita :", n.result, n.inspect())
see examples .
```

Links
-----
* PyPI_
* GitHub_
* .. _PyPI: http://pypi.python.org/pypi/nudepy/
* .. _GitHub: https://github.com/hhatto/nude.py