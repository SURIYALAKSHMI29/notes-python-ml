# HTTP

---

# Table of Contents

1. [Web Server-Client](#web-server-client)
2. [WWW - World Wide Web](#www---world-wide-web)
3. [HTTP - Hyper Text Transfer Protocol](#http---hyper-text-transfer-protocol)

   * [HTTP Session](#http-session)
   * [Status Code](#status-code)
   * [IP Address](#ip-address)
   * [Compression in HTTP](#compression-in-http)
   * [HTTP Caching](#http-caching)
   * [HTTP Authentication](#http-authentication)
   * [HTTP Cookies](#http-cookies)
   * [HTTP vs HTTPS](#http-vs-https)
   * [TLS/SSL](#tlssl)
   * [Content Negotiation](#content-negotiation)

---

## Web Server-Client

* Server → serve web pages
* Client → browsers

## WWW - World Wide Web

* [www.google](http://www.google).com and google.com → both works
* Here www is used to identify the site as website (not necessary)

# HTTP - Hyper Text Transfer Protocol

* A protocol → defines set of conventions that dictate how a client talks with the web server
* Stateless protocol →Http cookies allow the use of stateful sessions
* Used for fetching resources such as HTML documents
* **Http versions**

  * *HTTP/1.0* → open a separate TCP connection for each http request / response pair
  * *HTTP/1.1* → introduced pipelining; TCP connection can be partially controlled; human readable
  * *HTTP/2* → Multiplexing messages over a single connection; Messages are embedded  into a binary structure, a frame
  * *HTTP/3 - HTTP over QUIC* → uses QUIC instead of TCP

    * QUIC → runs multiple streams over UDP and implements packet loss detection and retransmission independently for each stream, , so that if an error occurs, only the stream with data in that packet is blocked.
* Http request has Method name, Version, Host, Content type, Dest IP, Source IP, type of service
* Http response has Version, Status Code and message, Content types, content, content length

## HTTP session

1. Client establishes a connection
2. Client sends its request, and waits for the answer
3. Server processes the request, sending back its answer, providing a status code and appropriate data

### Status Code

200 → ok

301 → Moved permanently

303 → Found

401 →Unauthorized

403 → Forbidden

404 → not found

500 → Internal server error (Segmentation fault)

## IP Address

* Every device has unique IP address → which is of 32 bits (0.0.0.0 to 255.255.255.255)
* Useful for servers that are routing http requests and responses

## Compression in HTTP

* Both browsers and servers have already implemented compression mechanisms
* Happens at three different levels

### File format compression

* Loss-less compression

  * decompression cycle doesn’t alter the data that is recovered.
  * Matches byte-to-byte with the original.
  * Example: gif or png
* Lossy compression

  * Where the cycle alters the original data
  * Example: .jpeg image format, video

### End-to-End compression

* Compression of the body of a message → done by the server and will last unchanged until it reaches the client

![httpenco1.svg](attachment:7fb5e99d-b610-46ba-bf05-17ad0025420a.svg)

* Optimized for text

### Compression defined at the connection level

* To select the algo to use, browsers and servers use Proactive Content Negotiation
* Browser sends an Accept-Encoding header with the algorithm it supports, the server picks one, uses it to compress the body of the response and uses the Content-Encoding header to tell the browser the algo it has chosen

![httpcompression1.svg](attachment:36355b0c-de2c-40c0-9313-6139b18ac596.svg)

## HTTP Caching

* Stores a response associated with a request and reuses the stored response for subsequent requests

### Types of caches

* Private Cache → tied to a specific client(browser cache)
* Shared cache → Located between the client and the server and can store responses that can be shared among users.
* Heuristic caching → Even if no *Cache-Control* is given, responses will get stored and reused if certain conditions are met

  * For ex: Response that was updated 1 year ago, most probably will remain the same. In such cases, stored as cache in client side

### Fresh and stale based on age

* Fresh →If the age of the response is less than the max-age
* Stale → If the age of the response is more than the max-age
* If the cached response if fresh, then it will be sent back to the clients, otherwise process the request again

### Validation

* Stale responses are not discarded immediately
* Http has a mechanism to transform a stale response into a fresh one by asking the origin server → called *validation* or *revalidation*
* If the response becomes stale and the cache cannot be reused → So request the client sending a request with an ***If-Modified-Since*** request header, to ask the server if there have been any changes made since the specified time
* The server will respond with *304 Not Modified* if it has not changed since the specified time → the response became fresh and restart the expiry time
* Problems → distrubuted servers have difficulty in synchronizing file-update times
* *Last-Modified and ETag headers*  → helps in validation

### Cache-Control

**Cache-Control: no-cache**

* Similar to *max-age=0* and *must-revalidate* combination
* Doesn’t prevent the storing of responses but instead prevents the reuse of responses without revalidation

**Cache-Control: no-store**

* Response will not be stored anywhere
* prevents from storing, but does not delete any already-stored response for the same URL

**Cache-Control: private**

* Response will not be stored by anyone other than the specific client, for privacy
* Provide up-to date content everytime

## HTTP authentication

* 401 Unauthorized response + www - authentication header

![basic-auth.svg](attachment\:bd327dc7-3a39-46e1-b040-4739b6a7fb3a.svg)

* If the credentials are invalid → 401
* Valid, but user lacks permission → 403 Forbidden

> Sends the credentials encoded but not encrypted → insecure unless the exchange was over a secure connection (HTTPS/TLS)

* Proxy Authentication → Requires authentication at proxy server level

## HTTP cookies

* Small piece of data a server sends to a user’s web browser; The browser may store, create or modify the cookies and send them back to the same server with later requests

* Create/Update Cookies

  ```
  Set-Cookie: <cookie-name>=<cookie-value>
  ```

* To delete → define lifetime of the cookie

  ```
  Set-Cookie: id=a3fWa; Expires=Thu, 31 Oct 2021 07:28:00 GMT;

  or

  Set-Cookie: id=a3fWa; Max-Age=2592000
  ```

* Session cookies → cookies without Max-Age or Expires attribute are deleted when the current session ends.

  * Some browser use session restoring when restarting → cause session cookies to last indefinitely

### Security & Scope

* Secure → only send over HTTPS
* HttpOnly → not accessible to JavaScript
* Domain and Path → scope of where the cookie is sent
* SameSite → controls whether cookie is sent on cross-site requests

  * Helps to prevent leakage of Information, preserving user privacy
  * Takes three possible values as

    * Strict → browser will send cookie only if the request originates from the same site
    * Lax → browser will also send it if the user navigates to the site via a link from another site (Default is Lax)
    * None → browser sends it even for requests initiated from another site, but must be HTTPS (Secure)

## HTTP vs HTTPS

* HTTP (80 port) → Transfers data in plain text. Anyone intercepting the traffic can read the sensitive info like usernames, passwords
* HTTPS (443 port) → HTTP over TLS/SSL; Encrypts data before sending it, so even someone intercepts it, they cannot read it
* Cookies with Secure attribute can only be sent over HTTPS

## TLS/SSL

* SSL(Secure Socket Layer)→ older version

  * Uses encryption algorithms to protect data during transmission
  * Verifies the identity of the server(via certificate) before sharing data
  * Ensures data has not been altered during the transmission
* TLS (Transport Layer Security) → successor of SSL

  * Uses stronger encryption algorithms
  * Forward Secrecy → even if the server’s private key is leaked later, past session data can’t be decrypted

### Keys

* TLS starts with public key cryptography(asymmetric) →server has public key(encrypt data) and private key(decrypt data)
* Using a session key (symmetric encryption) after handshake, used by both client and server to encrypt/decrpt messages
* Symmetric encryption is faster than asymmetric

## Content Negotiation

* Allows the server to serve different representations (HTML, JSON, XML, different languages, encodings) from the same URI based on what the client prefers

### Two Primary mechanisms

1. **Server-driven(proactive) Negotiation**
    * The client sends the specific HTTP headers indicating its preferences, and the server uses these to select the appropriate representation
    * Common headers as,
        * *Accept*: Specifies acceptable media types
        * *Accept-Language*: Indicates preferred languages
        * *Accept-Encoding*: Lists acceptable encoding
    * The server responds with best match and returns it
    * Errors if no representation is found
        * 406 → Not Acceptable
        * 415 → Unsupported Media Type
    * Most Common approach
2. **Agent-driven(Reactive) Negotiation**
    * Client requests the resource
    * Server returns the list of appropriate representations with the code 300 → Multiple choices
    * Client requests the specific representation
    * Server returns the requested representation
    * **Drawbacks**
        * HTTP standard doesn’t specify the format of the page for choosing between available resources →prevents the process from being automated
        * One more request is needed to fetch the real resource → slow
