use hyper::{Body, Response, Request, Server}
use hyper::service::{make_service_fn, service_fn};

async function handle_request{req: Request<Body>} -> Result{Response<Body>}

    // This is where our gateway logic will reside
    Ok(Response::new(Body::from("Hello, World!")))
    
