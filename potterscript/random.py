"""Random generator of potterscript."""

from potterscript import spells, quotes

def spell():
	return spells.gen_random()

def quote():
	return quotes.gen_random()
