use env_logger;

use actix_files::Files;
use actix_web::{web, App, HttpResponse, HttpServer};
use log::debug;

// mod utils;
// mod extra_handlers;
// mod swagger_docs;
// mod types;
mod extra_handlers;
mod swagger_docs;

use crate::swagger_docs::ApiDoc;
use utoipa::OpenApi;
use utoipa_swagger_ui::SwaggerUi;

#[actix_web::main] // or #[tokio::main]
async fn main() -> std::io::Result<()> {
    std::env::set_var("RUST_LOG", "debug"); // info
    std::env::set_var("RUST_BACKTRACE", "1");

    env_logger::init();
    debug!("timeproject25 service started");

    HttpServer::new(|| {
        App::new()
            .route("ok/", web::get().to(HttpResponse::Ok))
            .service(extra_handlers::response_html1)
            .service(
                SwaggerUi::new("/swagger/{_:.*}").url("/swagger/openapi.json", ApiDoc::openapi()),
            )
            .service(
                Files::new("/", "./dist/spa")
                    .index_file("index.html")
                    .path_filter(|path, _| {
                        debug!("path: '{}'", path.display());
                        true
                    }),
            )
    })
    .workers(4)
    .bind(("0.0.0.0", 8080))
    .expect("Can't bind server service on host:port")
    .run()
    .await
}
