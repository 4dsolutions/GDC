"""
PR to help kickstart global matrix
(c) MIT License, GDC
"""

from random import choice

the_table = [
"""
<td align="left">
<p>
Join an exclusive group of insiders, the first to receive Glenn Stockton&rsquo;s 
pioneering research into our shared Global Matrix, this world in which we 
live (&ldquo;the matrix&rdquo;) as seen through new lenses (remembering to think 
&ldquo;roundly&rdquo;).
</p>
<p>
Aspects of nature hitherto hiding in plain sight will leap to the 
foreground as Glenn&rsquo;s summarizing views strike chord after chord in your 
everyday experience.  
</p>
<p>
Fine tune your heuristics and find a future revealed, using &ldquo;the hexapent&rdquo; 
as your new crystal ball, and world gamer&rsquo;s paradise all rolled into one.
</p>
<p>
Glenn&rsquo;s series of publications will connect many dots already out there, 
saving you following trails of bread crumbs already decoded by a master 
&ldquo;decryptographer&rdquo;.  Follow Glenn&rsquo;s mental maps to still buried treasure.
</p>
<p>
In treating nature as a code, Glenn has found many keys, a set of memes 
for unlocking her secrets.  
</p>
<p>
Join Glenn at the front lines and get inspired with stories of your own, 
as you begin to grasp the torch he&rsquo;s passing.
</p>
<p>
Glenn&rsquo;s background as an NSA-trained cryptographer helped him discover 
the key mindset.  Let him take you into his world, as both autobiographer 
and tour guide.  
</p>
<p>
Some love of geometry required.
</p>
</td>
""", """
<td align="left">
<p>
Join an insider circle of savvy investors hot on the trail of the 
global Zeitgeist.  
</p><p>
Glenn noticed an emerging trend in the 1900s, away from rectilinear models 
and structures and towards a more sphere-friendly grid.  
</p><p>
He was not alone in experiencing this shift (great minds think alike), by 
definition of what we mean by Zeitgeist (or Noosphere if you prefer).  
Books like Beyond the Cube, and geodesic domes by Buckminster Fuller were
more harbingers of the &ldquo;new aesthetics&rdquo;.
</p><p>
He does have a front row seat however and is eager to share his perspective.  
Prepare to synergize, as you start to recognize, and share a sense of, the 
Global Matrix.
</p><p>
Fine tune your heuristics and find a future revealed, using &ldquo;the hexapent&rdquo; 
as your new crystal ball, and world gamer&rsquo;s paradise all rolled into one.
</p><p>
Glenn&rsquo;s series of publications will connect many dots already out there, 
saving you following trails of bread crumbs already decoded by a master 
&ldquo;decryptographer&rdquo;.  
</p><p>
In treating nature as a code, Glenn has discovered many keys.  Join him 
at the front lines and get inspired to weave new stories of your own 
incorporating these new memes.
</p><p>
Glenn&rsquo;s background as an NSA-trained cryptographer helped him discover 
the key mindset.  Let him take you into his world, as a storyteller and 
tour guide.  Some love of geometry required.
</p>
</td>
</tr>
""", """
<td align="left">
<p>
We&rsquo;ve all heard of the Matrix (hello Neo!) but do we remember it&rsquo;s round?  
We live on a spherical planet, not in a single grid-iron city of XY city 
blocks.  
</p><p>
Enter the hexagon with twelve pentagons as a way of tiling and 
we&rsquo;re back to a more globe friendly game board, data display, or &ldquo;macroscope&rdquo; 
if you will.
</p><p>
Fine tune your heuristics and find a future revealed, using &ldquo;the hexapent&rdquo; 
as your new crystal ball, and world gamer&rsquo;s paradise all rolled into one.
</p><p>
Join an insider circle of savvy investors hot on the trail of the global 
Zeitgeist.  
</p><p>
Glenn&rsquo;s series of publications will connect many dots already out there, 
saving you following trails of bread crumbs already decoded by a master 
&ldquo;decryptographer&rdquo;.  Glenn helps us crack nature&rsquo;s codes.  
Let him help 
you too.
</p><p>
In treating nature as a code, Glenn has discovered many keys.  Join him 
at the front lines and get inspired to weave new stories of your own 
incorporating these new memes.
</p><p>
Glenn&rsquo;s background as an NSA-trained cryptographer helped him discover 
the key mindset.  Let him take you into his world, as a storyteller and 
tour guide.  Some love of geometry required.
</p>
</td>"""]

web_page = \
"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    background-color: black;
}}

h2 {{
    color: yellow;
    margin-left: 40px;
}}
p {{
  font-family: "Times New Roman", Times, serif;
  color: yellow;
}}
</style>
<title>Kickstarting the Global Matrix</title>
</head>
<body>
<div align="center">
<table width="800" border="0" cellpadding="10">
<tr><td align="center">
<h2>Kickstarting the Global Matrix</h2>
<img src = "gmtest.jpg" />
</td></tr>
<tr>{}</tr>
</table>
</div>
</body>
</html>"""

output = web_page.format(choice(the_table))

f = open("global_matrix_serialized.html", "w")
print(output, file=f)
f.close()



