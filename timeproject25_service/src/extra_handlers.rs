// use askama::Template;
use actix_web::get;
use actix_web::{HttpResponse, HttpRequest, http::{header::ContentType, StatusCode}, Result};
// HttpRequest -> Result<HttpResponse, Error>

#[utoipa::path(responses((
    description = "HTML Answer with 404 status code",
    status = 404
)))]
#[get("/html1")]
// #[route("/test", method = "GET")]
pub async fn response_html1(req: HttpRequest) -> Result<HttpResponse> {
    println!("{req:?}");
    Ok(HttpResponse::build(StatusCode::NOT_FOUND)
            .insert_header(ContentType::html())
            .body("NOT FOUND!!!"))
}