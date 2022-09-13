def btccurce(course, usdt):
    btc = usdt / course
    cur_btc = 'Course BTC:', course
    have_us = 'How much BUSD do you have?:', usdt
    your_btc = 'Your BTC:', btc
    return cur_btc, have_us, your_btc
