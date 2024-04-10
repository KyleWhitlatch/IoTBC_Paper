// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
pragma abicoder v2;

import "@openzeppelin/contracts/utils/Strings.sol";

contract service_selector {

    uint constant iot_num = 100;

    mapping(uint=>Metrics) iot_sensors;


    uint randNonce = 0;
    constructor() public {
    }
   
    
    struct Metrics {
        uint latency;
        uint packetloss;
        uint jitter;
    }

function selector(uint[13] calldata request) external returns (uint[10] memory){
    uint user_latency = request[10];
    uint user_pl = request[11];
    uint user_jitter = request[12];
    uint[10] memory devices = [uint256(0), 0, 0, 0, 0, 0, 0, 0, 0, 0];
    for(uint x = 0; x < 10; x++){
        for(uint y = x; y < iot_num; y+=10){
                if (user_jitter > (random(4)-1) && user_latency > (random(100)) && user_pl > (random(30))){
                    devices[x] = y;
                }
        }
    }
    return devices;
}


function random(uint max) internal returns (uint) {
    uint randomnumber = uint(keccak256(abi.encodePacked(block.timestamp,msg.sender,randNonce))) % max;
    randomnumber = randomnumber + 1;
    randNonce++;
    return randomnumber;
}

}


