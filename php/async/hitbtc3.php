<?php

namespace ccxt\async;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use ccxt\async\abstract\hitbtc3 as hitbtc;

class hitbtc3 extends hitbtc {

    public function describe() {
        return $this->deep_extend(parent::describe(), array(
            'id' => 'hitbtc3',
            'alias' => true,
        ));
    }
}
