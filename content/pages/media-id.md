Title: Media IDs
Authors: Adam Dodman
Status: published

We always want our containers to work together where possible. This is doubly true for our media containers, that typically need to share files and data between them. To help with this goal, we have laid out a roadmap to prevent user ID conflicts, thereby making sure each application stays seperate and secure while still sharing needed resources.

Below is a table that shows the UIDs assigned to specific containers. Currently all of the UIDs are between 900 and 950. Crossed out applications represent a reserved UID, for an application where we do not have a functional container at this time.

The tens position of dictates the type of service it is, as in the table below:   

|No. | Software type|
|---:|---|
|00|Media downloaders|
|10|Software to interface with indexers|
|20|Media management and categorizing software|
|30|Alternates for 20, currently not used|
|40|Client facing media serving applications|
|50|Auxillary services that function with the frontend|

The full list of media applications:

|9XX|0X|1X|2X|3X|4X|5X|
|---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**1**|[NzbGet](https://github.com/spritsail/nzbget)|[NZBHydra](https://github.com/spritsail/nzbhydra)|[Sonarr](https://github.com/spritsail/sonarr)|[SickRage](https://github.com/spritsail/sickrage)|[Plex](https://github.com/spritsail/plex-media-server)|[Tautulli](https://github.com/spritsail/tautulli)|
|**2**|[Deluge](https://github.com/spritsail/deluge)|[Jackett](https://github.com/spritsail/jackett)|[Radarr](https://github.com/spritsail/radarr)|~~CouchPotato~~|~~Emby~~|[Ombi](https://github.com/spritsail/ombi)|
|**3**|~~Flood~~|~~Cardigann~~|[Lidarr](https://github.com/spritsail/lidarr)|~~Headphones~~|||
|**4**|||~~LazyLibrarian~~||||
|**5**|||~~Mylar~~||||
|**6**|||||||
|**7**|||||||
|**8**|||||||
|**9**|||||||

*Table current as of 16/07/18*
