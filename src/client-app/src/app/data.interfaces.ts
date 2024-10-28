export interface AccessToken {
  access_token : string
  token_type : string
}

export interface UserCredentials {
  username: string
  password: string
}


export interface TokenRequest {
  grant_type: string;
  username: string;
  password: string;
  scope?: string;
  client_id: string;
  client_secret: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  expires_in?: number;
  refresh_token?: string;
}
