import Foundation

let MAX_RETRIES = 3

/// Represents a user model.
struct User {
    let id: Int
}

/// Handles user operations.
class UserService {
    /// Retrieves a user by id.
    func getUser(userId: Int) -> User? {
        return nil
    }
}

/// Authenticate a token.
func authenticate(token: String) -> Bool {
    return !token.isEmpty
}

protocol Authenticatable {
    func authenticate(token: String) -> Bool
}
