---
title: {MASCOT_NAME} Rendering Test
description: This test page shows all mascot images as well as the admonition styles for our pedagogical agent {MASCOT_NAME}
image: img/mascot/welcome.png
og:image: img/mascot/welcome.png
---
# {MASCOT_NAME} - Mascot Test

This page shows all mascot images as well as the admonition styles for reference. Check that all the images have a transparent background
and do not have excessive padding around the drawing.
Note that the images have a dashed blue border around them so you can clearly see the padding.

<style type="text/css">
  img {
    border: 1px dashed blue;
  }
</style>



## Admonition Tests


!!! mascot-neutral "A Note from {MASCOT_NAME}"
    <img src="../../img/mascot/neutral.png" class="mascot-admonition-img" alt="{MASCOT_NAME} notes">
    Here is a friendly note from {MASCOT_NAME}.

!!! mascot-welcome "{MASCOT_NAME} Welcomes You!"
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="{MASCOT_NAME} welcomes you">
    Welcome, friend!

!!! mascot-thinking "{MASCOT_NAME} Key Insight"
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="{MASCOT_NAME} is thinking">
    Let's think this through together!

!!! mascot-tip "{MASCOT_NAME}'s Tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="{MASCOT_NAME} shares a tip">
    Here is a helpful suggestion.

!!! mascot-warning "{MASCOT_NAME} Gentle Warning of Common Mistake"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="{MASCOT_NAME} warns you">
    Watch out for this one!  It can be tricky!

!!! mascot-encourage "You've Got This!"
    <img src="../../img/mascot/encouraging.png" class="mascot-admonition-img" alt="{MASCOT_NAME} encourages you">
    You can do it!  I have faith in you!

!!! mascot-celebration "Excellent Work!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="{MASCOT_NAME} celebrates">
    Congratulations!  You made it!


## Image Padding Tests

Verify that there is no excessive padding around the images.
If there is, run the Python script that removes the extra padding.

<div class="grid cards" markdown>
1. Welcome
![](../img/mascot/welcome.png){ width="150px"}
2. Thinking
![](../img/mascot/thinking.png){ width="150px"}
3. Tip
![](../img/mascot/tip.png){ width="150px"}
4. Warning
![](../img/mascot/warning.png){ width="150px"}
5. Encouraging
![](../img/mascot/encouraging.png){ width="150px"}
6. Celebration
![](../img/mascot/celebration.png){ width="150px"}
7. Neutral
![](../img/mascot/neutral.png){ width="150px"}
</div>