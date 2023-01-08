import { ERC721 } from "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract TheNFT is ERC721 {
    constructor() ERC721("Scroll L2 NFT", "SNFT") {
    }
}
