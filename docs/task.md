# Group Activity Recognition task specification

Status: draft. The organizers have chosen **balanced accuracy across the ten classes on one leaderboard**. Input-modality restrictions and all other rules remain to be finalized.

How do pixels and player positions contribute to understanding collective activities in football? Building on SN-GAR, this challenge explores group activity recognition using visual and positional information. Participants will investigate how these complementary representations help interpret the actions of players as a group.

## Decisions before launch

- [ ] Decide whether pixels, positions and fusion are all allowed on the common leaderboard, and specify exactly which input assets participants may use.
- [ ] Freeze allowed external data and pretrained models.
- [x] Primary ranking metric: balanced accuracy; one leaderboard.
- [ ] Confirm tie policy and final class vocabulary against the frozen reference.
- [ ] Map the real manifest IDs to submissions; ensure the held-out reference has every evaluated class.
- [x] Use the existing test split for ranking even though its ground truth is available to approved users.
- [ ] Define the required reproducibility package and verification process for the no-test-training rule.
