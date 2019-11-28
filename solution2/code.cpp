//line 742

float http_versionf;
try{
  http_versionf = std::stof(response->session->request->http_version);
} catch (std::exception e){
  http_versionf = 1.1;
}

if(http_versionf >= 1.1) {
auto new_session = std::make_shared<Session>(this->config.max_request_streambuf_size, response->session->connection);
this->read(new_session);
return;
