# Group Activity Recognition task specification

Status: draft; technical choices below are not final rules.

How do pixels and player positions contribute to understanding collective activities in football? Building on SN-GAR, this challenge explores group activity recognition using visual and positional information. Participants will investigate how these complementary representations help interpret the actions of players as a group.

## Decisions before launch

- [ ] Define pixel-only, position-only and optional fusion tracks.
- [ ] Freeze allowed external data and pretrained models.
- [ ] Confirm the primary ranking metric, tie policy and class vocabulary.
- [ ] Map the real manifest IDs to submissions; ensure the held-out reference has every evaluated class.
- [ ] Confirm whether existing test labels have been distributed and identify a genuinely held-out final split.
