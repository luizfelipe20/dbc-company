class Orders:
    number_trips = 0

    def combine_orders(self, requests: list, n_max: int) -> int:
        """
        Calculates the number of trips that need to be made based on a list of requests.

        args: 
            - requests: list of requests made            

        returns:
            Returns the number of trips to be made.
        """
        try:
            _first_elem = requests[0]
            _second_elem = requests[1]
            _total =_first_elem + _second_elem

            if _total <= n_max:
                self.number_trips += 1
                requests.pop(0)
                requests.pop(0)
            else:
                self.number_trips += 1
                requests.pop(0)
        except TypeError as exc:
            raise Exception(f"type_error__combine_orders: {exc}")
        except IndexError as exc:
            raise Exception(f"index_error__combine_orders: {exc}")

        if len(requests) > 1:
            return self.combine_orders(requests, n_max)

        self.number_trips += len(requests)

        return self.number_trips
