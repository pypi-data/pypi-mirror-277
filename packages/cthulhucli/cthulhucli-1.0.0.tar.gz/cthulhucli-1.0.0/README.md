Call of Cthulhu CLI
===================

A command line interface for browsing cards from [Call of Cthulhu CCG and LCG](https://www.fantasyflightgames.com/en/products/call-of-cthulhu-lcg/).

Install
-------

Call of Cthulhu CLI can be installed from [PyPI](https://pypi.python.org/pypi/cthulhucli) using pip:

    sudo pip install cthulhucli

Options
-------

Call of Cthulhu CLI has the following options as given by the --help option:

```console
$ cthulhucli --help
Usage: cthulhucli [OPTIONS] [TEXT]...

Options:
  --ccg          Search CCG era cards only.
  --lcg          Search LCG era cards only.
  -v, --verbose  Show more data.
  --brief        Show one line of data, regardless the level of verbose.
  --long         Show multiple lines of data, regardless the level of verbose.
  --show FIELD   Show given field only. Can be repeated to show multiple
                 fields in given order.
  --case         Use case sensitive filtering.
  --exact        Use exact match filtering.
  --regex        Use regular rexpressions when filtering.
  --or FIELD     Treat multiple tests for given field with logical
                 disjunction, i.e. OR-logic instead of AND-logic.
  --inclusive    Treat multiple tests for different fields with logical
                 disjunction, i.e. OR-logic instead of AND-logic.
  --sort FIELD   Sort results by given field.
  --desc         Sort results in descending order.
  --group FIELD  Group results by given field.
  --count FIELD  Print a breakdown of all values for given field.
  --version      Show the version and exit.
  --help         Show this message and exit.

Field filters:
  -n, --name TEXT         Filter on matching name.
  --descriptor TEXT       Filter on matching descriptor.
  --subtype TEXT          Filter on matching subtypes.
  -x, --text TEXT         Filter on matching text.
  --keyword TEXT          Filter on matching keywords.
  --unique                Filter on uniqueness.
  --non-unique            Filter on non-uniqueness.
  --faction FACTION       Filter on matching faction.
  --faction-isnt FACTION  Filter on non-matching faction.
  --type CARD TYPE        Filter on matching card type.
  --type-isnt CARD TYPE   Filter on non-matching card type.
  --cost NUMBER           Filter on matching cost (number comparison).
  --skill NUMBER          Filter on matching skill (number comparison).
  --terror NUMBER         Filter on number of terror icons.
  --combat NUMBER         Filter on number of combat icons.
  --arcane NUMBER         Filter on number of arcance icons.
  --investigation NUMBER  Filter on number of investigation icons.
  --set TEXT              Filter on matching set.
  --restricted            Filter on restricted.
  --non-restricted        Filter on non-restricted.
  --banned                Filter on banned.
  --non-banned            Filter on non-banned.

Where:
  CARD TYPE  One of: character, conspiracy, event, story, support.
  FACTION    One of: agency, cthulhu, hastur, miskatonic university, neutral,
             shub-niggurath, silver twilight, syndicate, the agency, yog-
             sothoth.
  FIELD      One of: banned, card type, cost, descriptor, faction, icons,
             keywords, name, restricted, set, skill, subtypes, text,
             uniqueness.
  NUMBER     A number optionally prefixed by one of the supported comparison
             operators: ==, =, !=, !, <=, <, >=, >. With == being the default
             if only a number is given.
  TEXT       A text partially matching the field value. The --case, --regex
             and --exact options can be applied. If prefixed with ! the match
             is negated.
```

Examples
--------

Find a card by its name:

```console
$ cthulhucli --name Nyarlathotep
Nyarlathotep: Unique. Neutral. Character. Cost 0. Skill 6. [TTCCA].
Nyarlathotep: Unique. Neutral. Character. Cost 4. Skill 4. [TCAI].
Nyarlathotep: Unique. Neutral. Character. Cost 5. Skill 6. [TCAI].

Total count: 3
```

Print more of the cards' information:

```console
$ cthulhucli --name Nyarlathotep -v
Nyarlathotep
The Crawling Chaos
Ancient One.
Villainous. Toughness +4.
Each Avatar of Nyarlathotep character gains (T)(T).
Action: pay 3 to take control of an Avatar of Nyarlathotep character.
Unique: Yes
Faction: Neutral
Card Type: Character
Cost: 0
Skill: 6
Icons: TTCCA

Nyarlathotep
The Black Pharaoh
Ancient One.
Villainous. Toughness +2.
During the resource phase, if an opponent wishes to attach a resource to a domain, the resource must be chosen at random from his hand. (Choose the domain first, then randomly determine the resource.)
Unique: Yes
Faction: Neutral
Card Type: Character
Cost: 4
Skill: 4
Icons: TCAI

Nyarlathotep
The Crawling Chaos
Ancient One.
Villainous. Toughness +1. Resilient.
You may return an Avatar character to your hand to reduce the cost to play Nyarlathotep by 3.
Disrupt: When you succeed at a story to which Nyarlathotep is committed, sacrifice it to put an Avatar character into play from your hand committed to an unresolved story, if able.
Unique: Yes
Faction: Neutral
Card Type: Character
Cost: 5
Skill: 6
Icons: TCAI

Total count: 3
```

Find all events with the *Day* or *Night* subtype:

```console
$ cthulhucli --subtype day --subtype night --or subtype --type event
Blessed Dawn: The Agency. Event. Cost X.
The Punishing Sun: Miskatonic University. Event. Cost X.
Howl of Jackals: Cthulhu. Event. Cost X.
Enshrouded Sun: Hastur. Event. Cost X.
Screaming of the Spheres: Yog-Sothoth. Event. Cost X.
Buzzing of Locusts: Shub-Niggurath. Event. Cost X.
Blinding Light: Neutral. Event. Cost 4.
Calling Forth the Abyss: Neutral. Event. Cost 4.

Total count: 8
```

Find all non-unique Miskatonic *Investigator* characters from the CCG era, grouped by cost:

```console
$ cthulhucli --non-unique --faction misk --subtype investigator --ccg --group cost
[ Cost 1 ]

Campus Gumshoe: Miskatonic University. Character. Cost 1. Skill 2. [CA].
Graduate Assistant: Miskatonic University. Character. Cost 1. Skill 2. No Icons.
Reclusive Researcher: Miskatonic University. Character. Cost 1. Skill 1. [II].

[ Cost 2 ]

Absent-Minded Accountant: Miskatonic University. Character. Cost 2. Skill 1. [AI].
Civil Engineer: Miskatonic University. Character. Cost 2. Skill X. [AI].
Cryptozoologist: Miskatonic University. Character. Cost 2. Skill 3. [A].
Field Researcher: Miskatonic University. Character. Cost 2. Skill 1. [I].
Mad Genius: Miskatonic University. Character. Cost 2. Skill 2. No Icons.
Strange Librarian: Miskatonic University. Character. Cost 2. Skill 1. [A].
Student Archaeologist: Miskatonic University. Character. Cost 2. Skill 2. [I].

[ Cost 3 ]

Anthropology Advisor: Miskatonic University. Character. Cost 3. Skill 2. [C].
Classicist: Miskatonic University. Character. Cost 3. Skill 3. [III].
Local Historian: Miskatonic University. Character. Cost 3. Skill 1. [AI].
Natural Philosopher: Miskatonic University. Character. Cost 3. Skill 3. [AI].
Professor of Metaphysics: Miskatonic University. Character. Cost 3. Skill 2. [II].
Seeker of the Profane: Miskatonic University. Character. Cost 3. Skill 2. [AI].
Two-Fisted Archaeologist: Miskatonic University. Character. Cost 3. Skill 6. No Icons.

[ Cost 4 ]

Theology Professor: Miskatonic University. Character. Cost 4. Skill 4. [AAII].

[ Cost 5 ]

Professor of Archaeology: Miskatonic University. Character. Cost 5. Skill 3. [CI].

Total count: 19
```

Find all characters with struggle boosters, displaying their full text:

```console
$ cthulhucli --type char --text "\(\([CTAI]\)\)" --regex --show text
Cairo Mercenary: ((C))((C)).
Decommissioned Officer: ((C)).
Local Historian: ((I)).
Professor of Archaeology: ((I))((I)).
Elder Shoggoth: ((T)).
Servant of the Key: ((A)).
Relentless Stalker: Willpower. Toughness +1.
When you would uncommit Relentless Stalker from a story, you may choose to not uncommit it until the story is won.
((C)).
A Scheme of Byakhees: Forced Response: After you win a (T) struggle at a story to which A Scheme of Byakhees is committed, the losing player must either discard a card from his hand, or drive a character he controls insane.
((T))((T)).
Hastur: Lower the cost to play Hastur by 1 for each insane character in play.
Villainous. Invulnerability. Fast.
When you win a (T) struggle at a story, place a success token on that story.
((T)).

Total count: 9
```

Find all 0 cost characters and get a breakdown of their faction, icons and subtypes:

```console
$ cthulhucli --type char --cost 0 --count faction --count icons --count subtype
[ Faction counts ]

Neutral:               4
Yog-Sothoth:           3
Cthulhu:               2
Miskatonic University: 2
Silver Twilight:       2
Hastur:                2
Shub-Niggurath:        1
The Agency:            1

[ Icons counts ]

Terror:                10
Combat:                4
Arcane:                3
Investigation:         1

[ Subtypes counts ]

Cultist:               5
Conspirator:           2
Servitor:              2
Investigator:          2
Ancient One:           1
Phantom:               1
Independent:           1
Monster:               1
Student:               1
Artist:                1
Lodge:                 1

Total count: 17
```

Credits
-------

* All card data is copyright by [Fantasy Flight Games](https://www.fantasyflightgames.com/).
* Call of Cthulhu CLI is written by [Petter Nyström](mailto:jimorie@gmail.com).
