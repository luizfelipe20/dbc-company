class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    _dict_open_contracts = {}

    def get_top_n_open_contracts(self,
                                 open_contracts: list,
                                 renegotiated_contracts: list,
                                 top_n) -> list:
        """
        Search for open contracts.

        args: 
            - open_contracts: list of contracts
            - renegotiated_contracts: list of renegotiated contracts
            - top_n: number of contracts to be selected
        
        returns: 
            List of contracts with the highest outstanding balance.
        """

        try:
            self._set_indexes_contracts(open_contracts)
            self._remove_already_renegotiated_contracts(renegotiated_contracts)

            _contracts = self._dict_open_contracts.items()
            newlist = (k for k, _ in sorted(_contracts, reverse=True, key=lambda item: item[1]))
        except Exception as exc:
            raise Exception(f"error__get_top_n_open_contracts: {exc}")
        return list(newlist)[:top_n]

    def _remove_already_renegotiated_contracts(self, renegotiated_contracts: list) -> dict:
        """
        Removes from the list of contracts all contracts that have already been renegotiated. 

        args: 
            - renegotiated_contracts: list of contracts already renegotiated
        
        returns: 
            Removes already renegotiated contracts from the list of open contracts.
        """
        for contract in renegotiated_contracts:
            self._dict_open_contracts.pop(contract)

    def _set_indexes_contracts(self, open_contracts: list) -> dict:
        """
        Creates a structure to index contracts based on the user identifier, 
        to facilitate the search for that contract.

        args: 
            - open_contracts: open_contracts            

        returns:
            Indexes contracts in a dictionary.
        """
        for contract in open_contracts:
            self._dict_open_contracts[contract.id] = contract.debt
