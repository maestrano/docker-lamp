<?php

// Set proxy configuration globally in PHP
if (getenv("http_proxy") !== false ) {
  $proxy_host_port = str_replace("http://","",getenv("http_proxy"));
  stream_context_set_default(['http'=>['proxy'=>$proxy_host_port]]);
}
