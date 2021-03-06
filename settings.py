screen_width = 1280
screen_height = 720

block_map = [
    '666666666666',
    '444557755444',
    '333333333333',
    '222222222222',
    '111111111111',
    '            ',
    '            ',
    '            ',
    '            ']

color_legend = {
    '1': 'blue',
    '2': 'green',
    '3': 'red',
    '4': 'orange',
    '5': 'purple',
    '6': 'bronze',
    '7': 'grey',
}

gap_size = 2
block_height = screen_height / len(block_map) - gap_size
block_width = screen_width / len(block_map[0]) - gap_size
top_offset = screen_height // 30

upgrades = ['speed', 'laser', 'heart', 'size']
