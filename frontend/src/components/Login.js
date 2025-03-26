import React from "react";
import { useNavigate } from "react-router-dom";
import { GoogleLogin } from "react-google-login";

const Login = () => {
  const navigate = useNavigate();

  const handleLoginSuccess = (response) => {
    console.log("Login Success:", response.profileObj);
    navigate("/profile");
  };

  const handleLoginFailure = (response) => {
    console.log("Login Failed:", response);
  };

  return (
    <div>
      <h1>Login</h1>
      <GoogleLogin
        clientId="your_google_client_id"
        buttonText="Login with Google"
        onSuccess={handleLoginSuccess}
        onFailure={handleLoginFailure}
        cookiePolicy={"single_host_origin"}
      />
    </div>
  );
};

export default Login;
