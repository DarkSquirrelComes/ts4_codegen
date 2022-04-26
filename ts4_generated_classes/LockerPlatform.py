
import tonos_ts4.ts4 as ts4


class LockerPlatform(ts4.BaseContract):
    def __init__(
        self,

        tokenLocker=None,
        platform_id=None,
        
        clientCode=None,
        amountToLock=None,
        staticCell=None,
        inputCell=None,
        
        address=None,
        balance=None,
        keypair=None,
    ):
        keypair = keypair or ts4.make_keypair()
        if address:
            super().__init__(
                'LockerPlatform',
                ctor_params=None,
                initial_data=dict(),
                address=address,
                nickname='LockerPlatform',
            )
        else:
            super().__init__(
                'LockerPlatform',
                ctor_params=None,
                initial_data=dict(
                    tokenLocker=tokenLocker,
                    platform_id=platform_id,
                    
                ),
                keypair=keypair,
                balance=balance,
                nickname='LockerPlatform',
            )

            super().call_method(
                'constructor',
                params=dict(
                    clientCode=clientCode,
                    amountToLock=amountToLock,
                    staticCell=staticCell,
                    inputCell=inputCell,
                    
                ),
                private_key=self.private_key_,
            )


    


    @property
    def _pubkey(self):
        return self.call_getter('_pubkey')

    @property
    def _timestamp(self):
        return self.call_getter('_timestamp')

    @property
    def _constructorFlag(self):
        return self.call_getter('_constructorFlag')

    @property
    def tokenLocker(self):
        return self.call_getter('tokenLocker')

    @property
    def platform_id(self):
        return self.call_getter('platform_id')

    
