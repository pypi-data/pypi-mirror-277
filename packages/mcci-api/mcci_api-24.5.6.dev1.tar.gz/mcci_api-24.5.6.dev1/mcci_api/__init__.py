# SPDX-FileCopyrightText: 2024 osfanbuff63 <osfanbuff63@osfanbuff63.tech>
#
# SPDX-License-Identifier: MIT

"""Unofficial Pythonic bindings for the MCC Island API."""

from gql import Client, gql
from gql.transport.httpx import HTTPXAsyncTransport
from typing import Optional
import httpx
from .types import (
    Player,
    ProgressionData,
    TrophyData,
    CrownLevel,
    Status,
    Server,
    ServerCategory,
    Game,
    Currency,
    Collections,
    PartialPlayer,
    Social,
    Party,
    Rotation,
    Statistic,
    LeaderboardEntry,
)
import warnings
from ._exceptions import NoUsernameOrUUIDException, InvalidTrophyType
from datetime import datetime


class APIClient:
    """The main class, initializing the API client that this library is built off of."""

    def __init__(self, api_key: str, user_agent: str) -> None:
        """Initialize the MCC Island API client.

        Args:
            api_key (str): The API key to use. This can be generated on the [Noxcrew Gateway website](https://gateway.noxcrew.com). This is sensitive, so it is recommended to store this in a safe place.
            user_agent (str): An identifiable string to use as the User-Agent header, preferably including a way to contact you. Example: 'osfanbuff63/mcci-api-python email@example.com'
        """
        self.api_key = api_key
        self.user_agent = user_agent
        self.transport = HTTPXAsyncTransport(
            url="https://api.mccisland.net/graphql",
            headers={
                "X-API-KEY": f"{self.api_key}",
                "User-Agent": f"{self.user_agent}",
            },
        )
        self.schema = httpx.get("https://api.mccisland.net/graphql/schema").text

    async def get_player(
        self,
        uuid: Optional[str] = "",
        username: Optional[str] = "",
        trophy_type: Optional[str] = "SKILL",
        # convert_username_to_uuid: Optional[bool] = False,
    ) -> Player:
        """Get the data on a player.

        Args:
            uuid (str, optional): The UUID to look up. This is the recommended way to look up a player. At least one of `uuid` and `username` must be specified. Defaults to "".
            username (str, optional): The username to look up. This is not recommended on its own, because if the user changed their username and hasn't joined MCC Island since or if they haven't logged into MCC Island recently, this method will fail. Defaults to "".
            trophy_type (str, optional): Whether to use skill or style trophies. The only options are "SKILL" or "STYLE" (not case sensitive in this library). Defaults to "SKILL".

        Raises:
            NoUsernameOrUUIDException: _description_
            NoUsernameOrUUIDException: _description_

        Returns:
            Player: An object representing the player that was looked up.
        """
        if (
            trophy_type.casefold() != "SKILL".casefold()  # type: ignore
            and trophy_type.casefold() != "STYLE".casefold()  # type: ignore
        ):
            raise InvalidTrophyType()
        if uuid:
            final_uuid = uuid
        elif username:
            # TODO: try and fix `convert_username_to_uuid`
            # if convert_username_to_uuid:
            # make a request to the Mojang API to see what this username's UUID is
            # url = f"https://api.minecraftservices.com/minecraft/profile/lookup/bulk/byname"
            # try:
            # response = httpx.post(url, content=f"['{username}']")
            # response.raise_for_status()
            # except httpx.HTTPError as e:
            # e.add_note("Make sure the username you provided was valid!")
            # raise httpx.HTTPError from e
            # final_uuid = response.json()["id"]
            warnings.warn(
                "Warning: `username` was provided and `uuid` was not, proceed at your own risk!"
            )
        else:
            raise NoUsernameOrUUIDException()
        try:
            if final_uuid:
                async with Client(
                    transport=self.transport, schema=self.schema
                ) as session:
                    query = gql(
                        # notes on this:
                        # - only query the uuid and username of friends and party members to let you manually look it up
                        #   - there will probably be a shortcut method for this in the `Player` object at some point
                        # - don't request statistics because it will be much easier to do in a separate method in the `Player` object
                        """
                    query player($uuid: UUID!) {
                        player(uuid: $uuid) {
                            uuid
                            username
                            ranks
                            crownLevel {
                                level nextEvolutionLevel nextLevelProgress {obtained obtainable} trophies {obtained obtainable bonus}
                            }
                            status {
                                online server {category subType associatedGame} firstJoin lastJoin
                            }
                            collections {
                                currency {coins gems royalReputation silver materialDust}
                            }
                            social {
                                friends {uuid username} party {active leader {uuid username} members {uuid username}}
                            }
                        }
                    }
                    """
                    )
                    variables = {"uuid": f"{final_uuid}", "category": f"{trophy_type}"}
                    # print(variables)
                    query_result = await session.execute(
                        query, variable_values=variables
                    )
        except UnboundLocalError:
            if username:
                async with Client(
                    transport=self.transport, schema=self.schema
                ) as session:
                    query = gql(
                        """
                    query playerByUsername($username: String!) {
                        playerByUsername(username: $username) {
                            uuid
                            username
                            ranks
                            crownLevel {
                                level nextEvolutionLevel nextLevelProgress {obtained obtainable} trophies {obtained obtainable bonus}
                            }
                            status {
                                online server {category subType associatedGame} firstJoin lastJoin
                            }
                            collections {
                                currency {coins gems royalReputation silver materialDust}
                            }
                            social {
                                friends {uuid username} party {active leader {uuid username} members {uuid username}}
                            }
                        }
                    }
                    """
                    )
                    variables = {
                        "username": f"{username}",
                        "category": f"{trophy_type}",
                    }
                    query_result = await session.execute(
                        query, variable_values=variables
                    )
            else:
                raise NoUsernameOrUUIDException()
        _query_player = query_result["player"]
        _player_uuid = _query_player["uuid"]
        _player_username = _query_player["username"]
        _player_ranks = _query_player["ranks"]

        _player_crown = _query_player["crownLevel"]
        _player_crown_level = _player_crown["level"]
        _player_crown_next_evolution_level = _player_crown["nextEvolutionLevel"]
        _player_crown_next_level = _player_crown["nextLevelProgress"]
        _player_crown_next_level_progress = ProgressionData(
            obtained=_player_crown_next_level["obtained"],
            obtainable=_player_crown_next_level["obtainable"],
        )
        _player_crown_trophy = _player_crown["trophies"]
        _player_crown_trophies = TrophyData(
            _player_crown_trophy["obtained"],
            obtainable=_player_crown_trophy["obtainable"],
            bonus=_player_crown_trophy["bonus"],
        )
        _player_crown_data = CrownLevel(
            _player_crown_level,
            _player_crown_next_evolution_level,
            _player_crown_next_level_progress,
            _player_crown_trophies,
        )

        _player_status_raw = _query_player["status"]
        _player_status_online = _player_status_raw["online"]
        # only populated if `online` is true
        try:
            _player_status_server_raw = _player_status_raw[""]
        except KeyError:
            _player_status_server_raw = None
        # escape the try/except so another can be used
        if _player_status_server_raw:
            _player_status_server_category = ServerCategory(
                _player_status_server_raw["category"]
            )
            try:
                _player_status_server_subtype = ServerCategory(
                    _player_status_server_raw["subtype"]
                )
            except KeyError:
                _player_status_server_subtype = None
            try:
                _player_status_server_associated_game = Game(
                    _player_status_server_raw["associatedGame"]
                )
            except KeyError:
                _player_status_server_associated_game = None
            _player_status_server = Server(
                _player_status_server_category,
                _player_status_server_subtype,
                _player_status_server_associated_game,
            )
        else:
            _player_status_server = None
        _player_status_first_join = datetime.fromisoformat(
            _player_status_raw["firstJoin"]
        )
        _player_status_last_join = datetime.fromisoformat(
            _player_status_raw["lastJoin"]
        )
        _player_status = Status(
            _player_status_online,
            _player_status_server,
            _player_status_first_join,
            _player_status_last_join,
        )

        _player_collections_raw = _query_player["collections"]
        _player_collections_currency_raw = _player_collections_raw["currency"]
        _player_collections_currency_coins = _player_collections_currency_raw["coins"]
        _player_collections_currency_gems = _player_collections_currency_raw["gems"]
        _player_collections_currency_royal_reputation = (
            _player_collections_currency_raw["royalReputation"]
        )
        _player_collections_currency_silver = _player_collections_currency_raw["silver"]
        _player_collections_currency_material_dust = _player_collections_currency_raw[
            "materialDust"
        ]
        _player_collections_currency = Currency(
            _player_collections_currency_coins,
            _player_collections_currency_gems,
            _player_collections_currency_royal_reputation,
            _player_collections_currency_silver,
            _player_collections_currency_material_dust,
        )
        _player_collections = Collections(_player_collections_currency)

        try:
            _player_social_raw = _query_player["social"]
        except KeyError:
            _player_social_raw = None
        if _player_social_raw:
            _player_social_friends = _player_social_raw["friends"]
            _player_social_friends_list = []
            for friend in _player_social_friends:
                _friend = PartialPlayer(friend["uuid"], friend["username"])
                _player_social_friends_list.append(_friend)
            _player_social_party = _player_social_raw["party"]
            _player_social_party_active = _player_social_party["active"]
            try:
                _player_social_party_leader_player = _player_social_party["leader"]
                _player_social_party_leader = PartialPlayer(
                    _player_social_party_leader_player["uuid"],
                    _player_social_party_leader_player["username"],
                )
            except KeyError:
                _player_social_party_leader = None
            try:
                _player_social_party_members = _player_social_party["members"]
                _player_social_party_members_list = []

                for member in _player_social_party_members:
                    _member = PartialPlayer(member["uuid"], member["username"])
                    _player_social_party_members_list.append(_member)
            except KeyError:
                _player_social_party_members_list = None
            _player_social_party = Party(
                _player_social_party_active,
                _player_social_party_leader,
                _player_social_party_members_list,
            )
            _player_social = Social(_player_social_friends_list, _player_social_party)
        else:
            _player_social = None

        return Player(
            _player_uuid,
            _player_username,
            _player_ranks,
            _player_crown_data,
            _player_status,
            _player_collections,
            _player_social,
        )
        # TODO: add a way to get style trophy numbers additionally (probably a method in the Player class?)

        # TODO: `statistics` query - assemble Statistic objects based on the elements given
        # TODO: `statistic` query - assemble a single Statistic object
        # possibly combine the logic for these two in a private function
        # TODO: find some way to make the nextRotation and previousRotation in the Rotation class
        # to make this work, we need to somehow get the api key and user agent into that class. probably easiest to have the user handle it themselves if they want to use that method
        # alternatively we can have that in this class and instead provide a Rotation object here

    async def next_rotation(self, rotation: Rotation) -> datetime:
        """Get the next rotation from a given rotation.

        Args:
            rotation (Rotation): The pre-defined Rotation to get the next rotation from.

        Returns:
            datetime: A `datetime.datetime` object representing the date and time of the next rotation.
        """
        async with Client(transport=self.transport, schema=self.schema) as session:
            query = gql(
                """
                    query nextRotation($rotation: Rotation!) {
                        nextRotation(rotation: $rotation)
                    }
                """
            )
            variables = str({"rotation": f"{rotation.value.upper()}"})
            query_result = await session.execute(query, variable_values=variables)
        result = query_result.get("data")["nextRotation"]
        return datetime.fromisoformat(result)

    async def previous_rotation(self, rotation: Rotation) -> datetime:
        """Get the previous rotation from a given rotation.

        Args:
            rotation (Rotation): The pre-defined Rotation to get the previous rotation from.

        Returns:
            datetime: A `datetime.datetime` object representing the date and time of the previous rotation.
        """
        async with Client(transport=self.transport, schema=self.schema) as session:
            query = gql(
                """
                    query previousRotation($rotation: Rotation!) {
                        previousRotation(rotation: $rotation)
                    }
                """
            )
            variables = str({"rotation": f"{rotation.value.upper()}"})
            query_result = await session.execute(query, variable_values=variables)
        result = query_result.get("data")["previousRotation"]
        return datetime.fromisoformat(result)

    async def get_single_statistic(self, key: str) -> Statistic:
        """Get a single statistic from its key.

        Args:
            key (str): The key representing the statistic. A list of keys is available at <insert url to docs here>

        Returns:
            Statistic: An object representing the data on this statistic.
        """
        async with Client(transport=self.transport, schema=self.schema) as session:
            query = gql(
                """
                query statistic($key: String!) {
                    statistic(key: $key) {
                        key
                        forLeaderboard
                        rotations
                        leaderboard {
                            rank
                            player {
                                uuid 
                                username
                            }
                        }
                    }
                }
                """
            )
            variables = str({"key": f"{key}"})
            query_result = await session.execute(query, variable_values=variables)
        _query_data = query_result.get("data")
        _statistic_data = _query_data["statistic"]
        _statistic_key: str = _statistic_data["key"]
        _statistic_for_leaderboard: bool = _statistic_data["forLeaderboard"]
        _statistic_rotations = []
        for rotation in _statistic_data["rotations"]:
            _rotation = Rotation(rotation)
            _statistic_rotations.append(_rotation)

        if _statistic_for_leaderboard:
            _statistic_leaderboard_entry = []
            for leaderboard_entry in _statistic_data["leaderboard"]:
                _leaderboard_entry_rank = leaderboard_entry["rank"]
                _leaderboard_entry_value = leaderboard_entry["value"]
                try:
                    _leaderboard_entry_player_raw = leaderboard_entry["player"]
                    _leaderboard_entry_player = PartialPlayer(
                        _leaderboard_entry_player_raw["uuid"],
                        _leaderboard_entry_player_raw["username"],
                    )
                except KeyError:
                    # the player probably has API status disabled, continue the loop
                    _leaderboard_entry_player = None
                _leaderboard_entry = LeaderboardEntry(
                    _leaderboard_entry_rank,
                    _leaderboard_entry_value,
                    _leaderboard_entry_player,
                )
                _statistic_leaderboard_entry.append(_leaderboard_entry)

        else:
            _statistic_leaderboard_entry = None
        return Statistic(
            _statistic_key,
            _statistic_for_leaderboard,
            _statistic_rotations,
            _statistic_leaderboard_entry,
        )

    async def get_all_statistics(self) -> list[Statistic]:
        """Get all the statistics with all the data applied. This method may be slow, use at your own risk!"""
        async with Client(transport=self.transport, schema=self.schema) as session:
            query = gql(
                """
                query statistics {
                    statistics {
                        key
                        forLeaderboard
                        rotations
                        leaderboard {
                            rank
                            player {
                                uuid
                                username
                            }
                        }
                    }
                }
                """
            )
            query_result = await session.execute(query)
        _query_data = query_result.get("data")
        _statistic_data = _query_data["statistic"]
        _statistics = []
        for statistic in _statistic_data:
            _statistic_key = statistic["key"]
            _statistic_for_leaderboard = statistic["forLeaderboard"]
            _statistic_rotations = []
            for rotation in statistic["rotations"]:
                _rotation = Rotation(rotation)
                _statistic_rotations.append(_rotation)

            if _statistic_for_leaderboard:
                _statistic_leaderboard_entry = []
                for leaderboard_entry in statistic["leaderboard"]:
                    _leaderboard_entry_rank = leaderboard_entry["rank"]
                    _leaderboard_entry_value = leaderboard_entry["value"]
                    try:
                        _leaderboard_entry_player_raw = leaderboard_entry["player"]
                        _leaderboard_entry_player = PartialPlayer(
                            _leaderboard_entry_player_raw["uuid"],
                            _leaderboard_entry_player_raw["username"],
                        )
                    except KeyError:
                        # the player probably has API status disabled, continue the loop
                        _leaderboard_entry_player = None
                    _leaderboard_entry = LeaderboardEntry(
                        _leaderboard_entry_rank,
                        _leaderboard_entry_value,
                        _leaderboard_entry_player,
                    )
                    _statistic_leaderboard_entry.append(_leaderboard_entry)

            else:
                _statistic_leaderboard_entry = None
            _statistics.append(
                Statistic(
                    _statistic_key,
                    _statistic_for_leaderboard,
                    _statistic_rotations,
                    _statistic_leaderboard_entry,
                )
            )
        return _statistics
