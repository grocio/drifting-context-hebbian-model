# drifting-context-hebbian-model
This Hebbian model simulates the memory performance for a serial recall task by assuming drifting context.

# Assumptions
I assume that context drifts as time passes or each event happens. It suggests that the representation for the context of position 0 is closer to that of position 1 than that of position 2. The representations with close temporal proximity are similar to each other.

While several variables affect the results, here is an example of the similarity of the representations for the context in this model.

|Rep \ Rep|pos 0|pos 1|pos 2|pos 3|pos 4|pos 5|pos 6|pos 7|pos 8|
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
|pos 0|1.|0.48|0.23|0.1|0.05|0.03|0.02|0.01|0.01|
|pos 1|0.48|1.|0.48|0.23|0.1|0.05|0.03|0.01|0.01|
|pos 2|0.23|0.48|1.|0.48|0.22|0.1|0.05|0.02|0.01|
|pos 3|0.1|0.23|0.48|1.|0.48|0.23|0.11|0.05|0.02|
|pos 4|0.05|0.1|0.22|0.48|1.|0.48|0.23|0.11|0.05|
|pos 5|0.03|0.05|0.1|0.23|0.48|1.|0.48|0.24|0.11|
|pos 6|0.02|0.03|0.05|0.11|0.23|0.48|1.|0.48|0.23|
|pos 7|0.01|0.01|0.02|0.05|0.11|0.24|0.48|1.|0.48|
|pos 8|0.01|0.01|0.01|0.02|0.05|0.11|0.23|0.48|1.|

In this model, the representations for the context works as the representations for the positions, which are also used as cues for each item at each position. For example, when recalling the item at position 0, the representation for the position 0 is thought to serve as a cue.

# Results
An example of graphs for accuray and transposition errors is shown.

![graph](https://raw.githubusercontent.com/grocio/drifting-context-hebbian-model/master/accuracy_transposition.png)

The leftmost top graph shows the memory performance for an item at the position 0. X axis is recalled items' positions. Y axis is the probability of recall. The probability of the correct recall is round 0.54 (When recalling an item at position 0, that item is correctly recalled!). The transposition errors refers to the errors of recalling the item at a wrong position. For example, the probability of recall of an item at the position 1 is round 0.24. Compared to the transposition error for an item at position 1, the transposition error for an item at the other positions are relatively small. Because the context drifts, similarity of the positions declines as the interval of the positions increases.

The serial position curve is shown as below.

![graph](https://raw.githubusercontent.com/grocio/drifting-context-hebbian-model/master/serial_position_curve.png)

The graphs were created based on the matrix below (the values might not be the exactly same as the values used for the graphs).

|Cor \ Ans|item 0|item 1|item 2|item 3|item 4|item 5|item 6|item 7|item 8|
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
|item 0|0.54|0.24|0.11|0.05|0.02|0.01|0.01|0.|0.01|
|item 1|0.22|0.41|0.2|0.1|0.04|0.02|0.01|0.|0.|
|item 2|0.1|0.19|0.38|0.18|0.08|0.04|0.02|0.01|0.01|
|item 3|0.04|0.09|0.18|0.37|0.18|0.08|0.04|0.02|0.01|
|item 4|0.02|0.04|0.08|0.18|0.37|0.17|0.08|0.04|0.02|
|item 5|0.01|0.02|0.04|0.08|0.17|0.37|0.18|0.09|0.04|
|item 6|0.|0.01|0.02|0.04|0.09|0.18|0.38|0.19|0.1|
|item 7|0.|0.|0.01|0.02|0.04|0.09|0.2|0.42|0.22|
|item 8|0.01|0.|0.01|0.01|0.02|0.05|0.11|0.24|0.55|

For example, the values of the first row tell you about the responses when recalling the item at the position 0.
The on-diagonal values show the probabilities of correct recall.

# Future direction
The serial position curve seems a little flat. A sharper U-shaped curve might be better. One possible solution is to introduce additional psychological mechanism(s) and implement it(them) in this model. For example, output interference, which is progressive intereference, may play an important role in creating a sharp U-shaped curve.
