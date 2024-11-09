// filter for non Pixibot administrators


onRecordBeforeAuthWithOAuth2Request((e) => {
  class NotAuthorizedUserError extends Error {}

  /** Return credentials of the EirbConnect's Pixibot OID client.
   * @returns {{tokenEndpoint: string, clientId: string}} credentials
   */
  function getEirbConnectCredentials(e) {
    const eirbConnectTokenEndpoint = e.providerClient.tokenUrl();
    const eirbConnectClientId = e.providerClient.clientId();
    return {
      tokenEndpoint: eirbConnectTokenEndpoint, 
      clientId: eirbConnectClientId
    };
  }

  /** Throw an error if the user is not authorize to use the service.
   * @param {string} eirbConnectClientId 
   * @param {string} eirbConnectTokenEndpoint 
   * @param {string} userOIDAccessToken 
    */
  function checkUserAuthorization(
    eirbConnectClientId, eirbConnectTokenEndpoint, userOIDAccessToken
  ) {
    const authorizationRequestParams = new FormData(); 
    authorizationRequestParams.append(
      "grant_type", "urn:ietf:params:oauth:grant-type:uma-ticket"
    );
    authorizationRequestParams.append("audience", eirbConnectClientId);
    authorizationRequestParams.append("response_mode", "decision");
    try {
      const res = $http.send({
        url: eirbConnectTokenEndpoint,
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "Authorization": `Bearer ${userOIDAccessToken}`
        },
        body: authorizationRequestParams
      });
      const unauthorizedError = new NotAuthorizedUserError(
        "The user is not authorized to use this service."
      );
      if (res.statusCode === 403) throw unauthorizedError;
      console.log("successful status code:", res.statusCode);
      const data = res.json;
      if (!data.result) throw unauthorizedError;
    } catch (error) {
      if (!error instanceof NotAuthorizedUserError) console.error(error);
      throw error;
    }
  }


  function main() {
    if (!e.isNewRecord || !e.oAuth2User) return;
    const {
      tokenEndpoint: eirbConnectTokenEndpoint, clientId: eirbConnectClientId
    } = getEirbConnectCredentials(e);
    const userOIDAccessToken = e.oAuth2User.accessToken;
    checkUserAuthorization(
      eirbConnectClientId, eirbConnectTokenEndpoint, userOIDAccessToken
    );
  }
  main();
})
