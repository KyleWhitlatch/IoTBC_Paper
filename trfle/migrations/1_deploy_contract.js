const sc = artifacts.require("service_selector.sol");

module.exports = function(deployer) {
  deployer.deploy(sc);
};