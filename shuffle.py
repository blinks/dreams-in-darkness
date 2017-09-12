#!/usr/bin/env python
# Shuffle up a tarot deck.
import random

deck = {
  '0 The Fool',
  'I The Magician',
  'II The High Priestess',
  'III The Empress',
  'IV The Emperor',
  'V The Hierophant',
  'VI The Lovers',
  'VII The Chariot',
  'VIII Strength',
  'IX The Hermit',
  'X Wheel of Fortune',
  'XI Justice',
  'XII The Hanged Man',
  'XIII Death',
  'XIV Temperance',
  'XV The Devil',
  'XVI The Tower',
  'XVII The Star',
  'XVIII The Moon',
  'XIX The Sun',
  'XX Judgement',
  'XXI The World',
}

for suit in ['Wands', 'Cups', 'Swords', 'Coins']:
    for rank in '23456789':
        deck.add('%s of %s' % (rank, suit))
    for rank in ['Ace', '10', 'Page', 'Knight', 'Queen', 'King']:
        deck.add('%s of %s' % (rank, suit))

order = list(deck)
random.shuffle(order)
print '\n'.join(order)
