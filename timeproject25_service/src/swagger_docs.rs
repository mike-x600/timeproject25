use utoipa::{
    openapi::{
        self,
        // security::{Http, HttpAuthScheme, SecurityScheme},
    },
    Modify, OpenApi,
};

// use crate::types;
// use crate::extra_handlers;

#[derive(OpenApi)]
#[openapi(
    paths(
      super::extra_handlers::response_html1,
    //   super::extra_handlers::response_json2,
    //   super::extra_handlers::response_plaintext3,
      // super::extra_handlers::response_html_template4,
    ),
    components(
        schemas(
            // utoipa::TupleUnit,
            // types::GenericPostRequest,
            // types::GenericPostResponse,
            // types::GenericStringResponse,
            // types::PostRequest,
            // types::PostResponse,
        )
    ),
    tags((name = "BasicAPI", description = "A very Basic API")),
    modifiers(&SecurityAddon)
  )]
pub struct ApiDoc;

struct SecurityAddon;
impl Modify for SecurityAddon {
    fn modify(&self, _openapi: &mut openapi::OpenApi) {
        // NOTE: we can unwrap safely since there already is components registered.
        // let components = openapi.components.as_mut().unwrap();
        // components.add_security_scheme(
        //     "Token",
        //     SecurityScheme::Http(Http::new(HttpAuthScheme::Bearer)),
        // );
    }
}
