
import tonos_ts4.ts4 as ts4


class SafeMultisigWallet(ts4.BaseContract):
    def __init__(
        self,

        
        owners=None,
        reqConfirms=None,
        
        address=None,
        balance=None,
        keypair=None,
    ):
        keypair = keypair or ts4.make_keypair()
        if address:
            super().__init__(
                'SafeMultisigWallet',
                ctor_params=None,
                initial_data=dict(),
                address=address,
                nickname='SafeMultisigWallet',
            )
        else:
            super().__init__(
                'SafeMultisigWallet',
                ctor_params=None,
                initial_data=dict(
                    
                ),
                keypair=keypair,
                balance=balance,
                nickname='SafeMultisigWallet',
            )

            super().call_method(
                'constructor',
                params=dict(
                    owners=owners,
                    reqConfirms=reqConfirms,
                    
                ),
                private_key=self.private_key_,
            )


    def acceptTransfer(
        self,
        payload,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='acceptTransfer',
                params=dict(
                    payload=payload,
                    
                ),
            )
        else:
            return super().call_method(
                method='acceptTransfer',
                params=dict(
                    payload=payload,
                    
                ),
                private_key=self.private_key_,
            )

    def sendTransaction(
        self,
        dest,
        value,
        bounce,
        flags,
        payload,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='sendTransaction',
                params=dict(
                    dest=dest,
                    value=value,
                    bounce=bounce,
                    flags=flags,
                    payload=payload,
                    
                ),
            )
        else:
            return super().call_method(
                method='sendTransaction',
                params=dict(
                    dest=dest,
                    value=value,
                    bounce=bounce,
                    flags=flags,
                    payload=payload,
                    
                ),
                private_key=self.private_key_,
            )

    def submitTransaction(
        self,
        dest,
        value,
        bounce,
        allBalance,
        payload,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='submitTransaction',
                params=dict(
                    dest=dest,
                    value=value,
                    bounce=bounce,
                    allBalance=allBalance,
                    payload=payload,
                    
                ),
            )
        else:
            return super().call_method(
                method='submitTransaction',
                params=dict(
                    dest=dest,
                    value=value,
                    bounce=bounce,
                    allBalance=allBalance,
                    payload=payload,
                    
                ),
                private_key=self.private_key_,
            )

    def confirmTransaction(
        self,
        transactionId,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='confirmTransaction',
                params=dict(
                    transactionId=transactionId,
                    
                ),
            )
        else:
            return super().call_method(
                method='confirmTransaction',
                params=dict(
                    transactionId=transactionId,
                    
                ),
                private_key=self.private_key_,
            )

    def isConfirmed(
        self,
        mask,
        index,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='isConfirmed',
                params=dict(
                    mask=mask,
                    index=index,
                    
                ),
            )
        else:
            return super().call_method(
                method='isConfirmed',
                params=dict(
                    mask=mask,
                    index=index,
                    
                ),
                private_key=self.private_key_,
            )

    def getParameters(
        self,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='getParameters',
                params=dict(
                    
                ),
            )
        else:
            return super().call_method(
                method='getParameters',
                params=dict(
                    
                ),
                private_key=self.private_key_,
            )

    def getTransaction(
        self,
        transactionId,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='getTransaction',
                params=dict(
                    transactionId=transactionId,
                    
                ),
            )
        else:
            return super().call_method(
                method='getTransaction',
                params=dict(
                    transactionId=transactionId,
                    
                ),
                private_key=self.private_key_,
            )

    def getTransactions(
        self,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='getTransactions',
                params=dict(
                    
                ),
            )
        else:
            return super().call_method(
                method='getTransactions',
                params=dict(
                    
                ),
                private_key=self.private_key_,
            )

    def getTransactionIds(
        self,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='getTransactionIds',
                params=dict(
                    
                ),
            )
        else:
            return super().call_method(
                method='getTransactionIds',
                params=dict(
                    
                ),
                private_key=self.private_key_,
            )

    def getCustodians(
        self,
        
        is_getter=False,
    ):
        if is_getter:
            return super().call_getter(
                method='getCustodians',
                params=dict(
                    
                ),
            )
        else:
            return super().call_method(
                method='getCustodians',
                params=dict(
                    
                ),
                private_key=self.private_key_,
            )

    


    
