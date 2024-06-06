# SPDX-FileCopyrightText: 2024 osfanbuff63 <osfanbuff63@osfanbuff63.tech>
#
# SPDX-License-Identifier: MIT

"""Objects used by the MCC Island API. Generally you shouldn't construct anything in here manually, it will be done by the library automatically."""

from __future__ import annotations
from typing import Optional
from enum import StrEnum
import datetime


class Collections:
    """The Collections object, which contains collections data."""

    def __init__(self, currency: Currency) -> None:
        """A representation of a player's collection data.

        Args:
            currency (Currency): The object which represents this player's earned currency.
        """
        self.currency = currency


class CrownLevel:
    """The CrownLevel object, which contains information regarding a player's Crown Level."""

    def __init__(
        self,
        level: int,
        next_evolution_level: int,
        next_level_progress: ProgressionData,
        trophies: TrophyData,
    ) -> None:
        """A Crown Level and associated trophy data.

        Args:
            level (int): The overall Crown Level.
            next_evolution_level (int): The next level that the crown will evolve, if any.
            next_level_progress (ProgressionData): The progress the player is making towards their next level, if any.
            trophies (TrophyData): The amount of trophies the player has.
        """
        self.level = level
        self.next_evolution_level = next_evolution_level
        self.next_level_progress = next_level_progress
        self.trophies = trophies


class Currency:
    """The Currency object, which contains a player's earned currency."""

    def __init__(
        self,
        coins: int,
        gems: int,
        royal_reputation: int,
        silver: int,
        material_dust: int,
    ) -> None:
        """A representation of a player's currency.

        Args:
            coins (int): The amount of Coins this player has earned.
            gems (int): The amount of Gems this player has earned.
            royal_reputation (int): The amount of Royal Reputation this player has earned.
            silver (int): The amount of Silver this player has earned.
            material_dust (int): The amount of coins this player has earned.
        """
        self.coins = coins
        self.gems = gems
        self.royal_reputation = royal_reputation
        self.silver = silver
        self.material_dust = material_dust


class Game(StrEnum):
    """Game enum."""

    HOLE_IN_THE_WALL = "HOLE_IN_THE_WALL"
    TGTTOS = "TGTTOS"
    BATTLE_BOX = "BATTLE_BOX"
    SKY_BATTLE = "SKY_BATTLE"
    PARKOUR_WARRIOR = "PARKOUR_WARRIOR"
    DYNABALL = "DYNABALL"
    ROCKET_SPLEEF = "ROCKET_SPLEEF"


class LeaderboardEntry:
    """An entry in a leaderboard."""

    def __init__(
        self,
        rank: int,
        value: int,
        player: Optional[Player] | Optional[PartialPlayer] | Optional[None] = None,
    ) -> None:
        """Initialize an entry in a leaderboard.

        Args:
            rank (int): The rank for this entry.
            value (int): The value for this entry.
            player (Player, optional): The player who has this entry. This will be `None` if the player does not have the statistics enabled for the API. However, for Crown Level or Trophy count leaderboards, the player will not be `None`. Defaults to None.
        """
        pass


class Party:
    """A player's status within a party."""

    def __init__(
        self,
        active: bool,
        leader: Optional[Player] | Optional[PartialPlayer] = None,
        members: Optional[list[Player]] | Optional[list[PartialPlayer]] = None,
    ) -> None:
        """Initialize an object representing a player's status within a party.

        Args:
            active (bool): Whether the player is in an active party.
            leader (Optional[Player], optional): The leader of the party, populated if the party exists. Defaults to None.
            members (Optional[list[Player]], optional): The members of the party, populated if the party exists. Defaults to None.
        """
        self.active = active
        self.leader = leader
        self.members = members


class Player:
    """The Player object, which contains many objects of information on a requested player. Construct via `APIClient.get_player()`."""

    def __init__(
        self,
        uuid: str,
        username: str,
        ranks: Optional[list[Rank]] = None,
        crown_level: Optional[CrownLevel] = None,
        status: Optional[Status] = None,
        collections: Optional[Collections] = None,
        social: Optional[Social] = None,
        statistics: Optional[Statistics] = None,
    ) -> None:
        """Initialize a Player object.

        Args:
            uuid (str): The player's Minecraft UUID in dashed format.
            username (str): The player's username, if known.
            ranks (Ranks, optional): The ranks which the user is associated with, if any.
            crown_level (CrownLevel, optional): The player's Crown Level and associated trophy data.
            status (Status, optional): The current status of the player. This method is conditional on the player having the in-game "status" API setting enabled.
            collections (Collections, optional): Collections data for the player. This method is conditional on the player having the in-game "collections" API setting enabled.
            social (Social, optional): Social data for the player. This method is conditional on the player having the in-game "social" API setting enabled.
            statistics (Statistics, optional): Statistics data for the player. This method is conditional on the player having the in-game "statistics" API setting enabled.
        """
        self.uuid = uuid
        self.username = username
        self.ranks = ranks
        self.crown_level = crown_level
        self.status = status
        self.collections = collections
        self.social = social
        self.statistics = statistics


class PartialPlayer(Player):
    """A partial player object that only contains a UUID and username."""

    def __init__(self, uuid: str, username: str) -> None:
        """Initialize a partial player object that only contains a UUID and username. To expand to a full Player object, use `APIClient.expand_partial_player` with this object.

        Args:
            uuid (str): The player's Minecraft UUID in dashed format.
            username (str): The player's username, if known.
        """
        super().__init__(uuid, username)


class ProgressionData:
    """An object that tracks some form of progression."""

    def __init__(self, obtained: int, obtainable: int) -> None:
        """Initialize an object that tracks some form of progression.

        Args:
            obtained (int): The amount of progression that has been obtained.
            obtainable (int): The amount of progression that is obtainable.
        """
        self.obtained = obtained
        self.obtainable = obtainable


class Rank(StrEnum):
    """Rank enum."""

    CHAMP = "CHAMP"
    GRAND_CHAMP = "GRAND_CHAMP"
    GRAND_CHAMP_ROYALE = "GRAND_CHAMP_ROYALE"
    CREATOR = "CREATOR"
    CONTESTANT = "CONTESTANT"
    MODERATOR = "MODERATOR"
    NOXCREW = "NOXCREW"


class Rotation(StrEnum):
    # TODO: add the nextRotation and previousRotation method here?
    """Rotation enum."""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"
    LIFETIME = "LIFETIME"


class Server:
    """A server on the MCC Island network."""

    def __init__(
        self,
        category: ServerCategory,
        sub_type: Optional[str] = None,
        associated_game: Optional[Game] = None,
    ) -> None:
        """Initialize an object representing a server on the MCC Island network.

        Args:
            category (ServerCategory): The category of the server.
            sub_type (str, optional): The sub-type of the server that can hold additional information about the server.
            associated_game (Game, optional): The game associated with this server, if any.
        """
        self.category = category
        self.sub_type = sub_type
        self.associated_game = associated_game


class ServerCategory(StrEnum):
    """Server Category enum."""

    LOBBY = "LOBBY"
    GAME = "GAME"
    LIMBO = "LIMBO"
    QUEUE = "QUEUE"


class Social:
    """A player's social data."""

    def __init__(
        self, friends: list[Player] | list[PartialPlayer], party: Party
    ) -> None:
        """Initialize an object which represents a player's social data.

        Args:
            friends (list[Player]): A list of the player's friends.
            party (Party): The player's party.
        """
        self.friends = friends
        self.party = party


class Statistic:
    """A statistic."""

    def __init__(
        self,
        key: str,
        for_leaderboard: bool,
        rotations: list[Rotation],
        leaderboard: Optional[list[LeaderboardEntry]] | Optional[None] = None,
    ) -> None:
        """An object that represents a statistic.

        Args:
            key (str): The key of the statistic.
            for_leaderboard (bool): If this statistic generates leaderboards.
            rotations: (list[Rotation]): The rotations for which this statistic is tracked. These are the rotations that can be used to generate leaderboards or fetch rotation values. Note that the `YEARLY` rotation never generates leaderboards, even if it is returned in this list.
            leaderboard: (list[LeaderboardEntry], optional): Returns the leaderboard for this statistic in a given rotation. If this statistic does not generate leaderboards, or the statistic is not tracked for the provided rotation, this will return None.
        """
        pass


class StatisticValueResult:
    """The result of fetching a value of a statistic."""

    def __init__(self, statistic: Statistic, value: int) -> None:
        """An object representing the result of fetching a value of a statistic.

        Args:
            statistic (Statistic): The statistic.
            value (int): The value.
        """
        self.statistic = statistic
        self.value = value

    def as_dict(self) -> dict:
        """Convert the stored value to a `dict` object."""
        stats_dict = {}
        stats_dict[self.statistic] = self.value
        return stats_dict


class Statistics:
    """Statistic-related data."""

    def __init__(self, value: StatisticValueResult) -> None:
        """An object representing statistic-related data.

        Args:
            value (StatisticValueResult): The raw value stored for this statistic.
        """
        self.value = value


class Status:
    """A player's current status."""

    def __init__(
        self,
        online: bool,
        server: Optional[Server] = None,
        first_join: Optional[datetime.datetime] = None,
        last_join: Optional[datetime.datetime] = None,
    ) -> None:
        """Initialize an object representing a player's current status.

        Args:
            online (bool): Whether the player is online or not.
            server (Server): The player's current server, if available.
            first_join (datetime.datetime, optional): When the player first joined MCC Island as a `datetime.datetime` object, if known. Defaults to None.
            last_join (datetime.datetime, optional): When the player most recently joined MCC Island as a `datetime.datetime` object, if known. Defaults to None.
        """
        self.online = online
        self.server = server
        self.first_join = first_join
        self.last_join = last_join


class TrophyData:
    """Data on the amount of the trophy progress of a player."""

    def __init__(self, obtained: int, obtainable: int, bonus: int) -> None:
        """Initialize an object representing data on the amount of the trophy progress of a player.

        Args:
            obtained (int): The amount of trophies obtained.
            obtainable (int): The amount of trophies obtainable.
            bonus (int): The amount of bonus trophies.
        """
        self.obtained = obtained
        self.obtainable = obtainable
        self.bonus = bonus
