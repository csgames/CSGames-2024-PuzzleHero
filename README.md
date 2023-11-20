# CSGames-2024-PuzzleHero

**Attention**, all challenges are valid in the puzzle Hero; quantity takes precedence above all! **All topics are allowed!**

A few small rules:

- Create a branch with the name of your challenge {category}-{name}
- Provide the description in English.

## Winning recipe for creating a challenge:

- [ ] 🚀 Have an idea
- [ ] 🔍 Check current or ongoing challenges to see if a similar challenge already exists
- [ ] 📝 Add a short description (1-2 sentence) to the kanban
- [ ] 🌿 Create a branch for the challenge
- [ ] 🏆 Complete your challenge
- [ ] 🛠️ Add the configuration.yml following [the provided template](./.github/challenge.yml)
- [ ] 📖 Write a writeup according to [the provided template](./.github/writeup.md)
- [ ] 🔄 Create a merge request

## Project structure

```
/challenges
  /<CATEGORY>
    /<CHALLENGE>
      challenge.yml       <-- IMPORTANT ! base yourself on the file .github/challenge-example.yml.
      ...                 <-- files for your challenge
      writeup.md          <-- outlines the solution, steps and thought process to solve challenge
      docker-compose.yml  <-- (if dockerized)

```

## Ports table

List of ports currently occupied by a challenge.

| Port    | Challenge                     | 
| :------ | :---------------------------- |
|         |                               |
