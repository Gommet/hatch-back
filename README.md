# Hatch API

This api was a project for HackUPC 2022. The aim of the project was to create a game similar to GeoCatching but inside the venue of the Hack and coperative between all people.

This api is easily integrable with any frontend. It has been developed using GraphQL so it makes even easyer the integration with front techs as Data can be queryed on-demand.

Eventhough we had not been on time to present you the API with a client, we want to let you know what is behind Hatch.

## Explanation of the idea

As it has been said, this API is all the back logic of a Game called Hatch. Staff and administrators of the hackathon will be able to prepare a "Session" in which they will be able to register some "Caches" that hackers will have to find. Those Chaches are especific objects, places that can be dispersed through all the venue. 

This is a colaborative game, this means that ALL HACKERS will be collaborating to find all the Caches that the Session contains. If one single Hacker finds one cache, all other hackers will go through the next level. 

Once a Cache is found, you can report this through a photo to the backend. There, we have an algorithm that computes the Image Similarity between the one updated by the administrator once created the Cache and the new submmited by the participant.

If the image is similar, which means that is the Cache, that cache will be marked as reached and the next one will appear.

Each cache has a determined the number of clues that are incrementally going public as the time without finding one passes.

## Technologies

Api entarelly build with Django-Graphene, a GraphQL library.

## Authors

Marta Alvets Mitjaneta, Sergi Simon Balcells, Oriol Alas Cercos, Joaquim Pico Mora, 