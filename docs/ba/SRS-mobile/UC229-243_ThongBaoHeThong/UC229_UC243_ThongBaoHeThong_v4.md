# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC229-243 — Nhắc hạn trên Mobile
**Ngày thực hiện:** 13/05/2026

**Phiên bản:** v6

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Thông báo |
| Đối tượng thực hiện | Cá nhân / Tổ chức (đã đăng nhập) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 29/04/2026 |
| Ngày cập nhật | 13/05/2026 |
| Phiên bản | v4.1 |


---

## UC229-243 — Nhắc hạn trên Mobile

### 1. Mô tả chức năng

**Tên chức năng:** Nhận thông báo hệ thống và kết quả xử lý hồ sơ trên Mobile  
**Mô tả:** Chức năng cho phép người dùng xem danh sách thông báo được hệ thống gửi đến. Thông báo bao gồm hai loại chính: thông báo hệ thống (UC258) và thông báo kết quả xử lý hồ sơ (UC259). Người dùng có thể xem chi tiết từng thông báo và đánh dấu đã đọc.  
**Phân quyền:** Cá nhân/Tổ chức đã đăng nhập.  
**Truy cập chức năng:** Trang chủ → Icon Thông báo (🔔) ở Header.  
- **Điều kiện kết thúc (Postconditions):** Trạng thái "Đã đọc" của thông báo được cập nhật đồng bộ trên hệ thống. Badge số lượng thông báo giảm tương ứng.
- **Chức năng đáp ứng usecase số:** UC229-243 (Phụ lục XIV — Nhóm E.II)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Thông báo

Header chứa nút Quay lại, tiêu đề "Thông báo", và nút Đánh dấu đã đọc tất cả (Icon tick đôi). Bên dưới là 2 tab: "Cảnh báo" và "Thông báo" (kèm badge số lượng chưa đọc màu đỏ).

#### 2.2 Màn hình Chi tiết Thông báo
*(Đã loại bỏ — wireframe không có màn hình chi tiết riêng. Tap vào card thông báo sẽ điều hướng theo Deep Link)*



#### 2.3 Phân loại và ưu tiên hiển thị thông báo

**(Lưu ý: Đây là "tag màu" phân loại thông báo, KHÔNG liên quan đến CMR-05 badge trạng thái. CMR-05 áp dụng cho badge trạng thái trên list item, còn bảng này dùng để phân biệt loại thông báo.)**

| Loại thông báo | Màu tag | Độ ưu tiên | Ví dụ nội dung |
|---|---|---|---|
| Kết quả xử lý hồ sơ | Xanh dương | Cao | "Hồ sơ [MÃ] của bạn đã được tiếp nhận". |
| Yêu cầu bổ sung hồ sơ | Cam | Cao | "Hồ sơ [MÃ] yêu cầu bổ sung tài liệu trước ngày...". |
| Thông báo hệ thống | Xám | Thấp | "Hệ thống bảo trì ngày XX/XX". |
| Nhắc hạn | Đỏ | Cao | "Hạn nộp báo cáo định kỳ còn 3 ngày". |

#### 2.4 Deep Link từ Push Notification

| Loại thông báo | Hành vi khi Tap vào Banner |
|---|---|
| Kết quả xử lý hồ sơ | Mở thẳng màn hình Chi tiết hồ sơ liên quan (UC46). |
| Yêu cầu bổ sung | Mở thẳng màn hình Chi tiết hồ sơ liên quan (UC46). |
| Thông báo hệ thống | Mở màn hình danh sách Thông báo (Tab Hệ thống). |
| Nhắc hạn | Mở màn hình phù hợp tùy theo loại nhắc (xem bảng mapping bên dưới). |

**Bảng mapping Deep Link cho loại "Nhắc hạn":**

| Loại nhắc hạn | Màn hình đích | UC liên quan |
|---|---|---|
| Nhắc bổ sung hồ sơ | Chi tiết hồ sơ | UC46 |
| Nhắc báo cáo định kỳ | Danh sách báo cáo / Tờ khai | UC63 / UC70 |
| Nhắc nghĩa vụ tài chính | Chi tiết nghĩa vụ tài chính | UC61 |
| Nhắc điều chỉnh dự án | Chi tiết dự án đầu tư | UC40 |
| Nhắc gia hạn dự án | Chi tiết dự án đầu tư | UC40 |
| Nhắc nghĩa vụ pháp lý phát sinh | Chi tiết hồ sơ | UC46 |

**Deep Link 404 Handling:**
Khi deep link trỏ đến hồ sơ/màn hình không tồn tại hoặc đã bị xóa → Hiển thị: *"Nội dung không tồn tại hoặc đã bị xóa."* (CMR-07)

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng xem danh sách
1. **Sort Order (2-tier):**
   - Tier 1: Độ ưu tiên **Cao → Thấp** (Cao: Kết quả hồ sơ, Yêu cầu bổ sung, Nhắc hạn; Thấp: Thông báo hệ thống)
   - Tier 2: Trong mỗi nhóm ưu tiên → Sort theo **thời gian giảm dần** (mới nhất trước)
2. **Lazy Load:** Tải 20 bản ghi/lần. Hỗ trợ nút "Tải lại" nếu API lỗi. (CMR-04)
3. **Debounce Interaction:** Chống double-tap khi mở card. (CMR-18)
4. **Pull to Refresh:** Hỗ trợ pull-to-refresh để tải lại danh sách. (CMR-13)
5. **Loading State:**
   - First-load: Skeleton loading toàn màn hình (CMR-07)
   - Lazy load: Spinner cục bộ ở cuối danh sách (CMR-04)
6. **Error Handling:**
   - API timeout/mất mạng: Toast lỗi + nút "Thử lại" (CMR-07, CMR-16)
   - Retry fail 3 lần (lazy load): Dừng, hiển thị lỗi cục bộ, pull-to-refresh để tải lại (CMR-04)
   - Thông báo lỗi: *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* / *"Hệ thống đang bận. Vui lòng thử lại sau."* / *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."*
7. **Empty State:** Khi danh sách rỗng → Hiển thị: *"Không có dữ liệu."* (CMR-14)
8. **Số ngày còn lại:**
   - Công thức: `Số ngày = Ngày đến hạn − Ngày hiện tại` (theo giờ server)
   - Hôm nay đến hạn → Hiển thị: **"Hôm nay"** (so sánh theo ngày, không tính giờ)
   - Đã quá hạn → Hiển thị: **"Đã quá hạn"** (không hiển thị số âm)
   - Cập nhật khi refresh danh sách
9. **Visual Read/Unread:**
   - **Chưa đọc:** Có **chấm đỏ** (badge dot) bên trái title + title **đậm (bold)**
   - **Đã đọc:** Không có chấm đỏ + title **bình thường (regular)**
10. **Badge số lượng:** Khi số thông báo > 99 → Hiển thị: **"99+"**

#### 3.2 Push Notification & i18n
1. **Foreground:** Hiện In-app Banner trong **3 giây**.
   - **Tap banner:** Điều hướng theo Deep Link (bảng 2.4).
   - **Dismiss banner:** Có thể vuốt để dismiss sớm. Không bắt buộc đợi hết 3 giây.
   - **Nhiều push liên tiếp:** Banner **thay thế** nhau (không xếp chồng) — banner mới đẩy banner cũ.
2. **Background:** Hiện Banner OS -> Tap mở app điều hướng theo Deep Link (mục 2.4).
3. **App Killed (not running):** Push notification OS-level vẫn hiển thị. Tap vào push -> Mở app -> Điều hướng theo Deep Link.
4. **New notification khi đang xem danh sách:** Tự động xuất hiện ở đầu danh sách (không cần refresh thủ công). Badge tăng tương ứng.
5. **i18n:** Nội dung server trả về theo ngôn ngữ người dùng tại thời điểm phát sinh tin.

#### 3.3 Đồng bộ trạng thái
1. **Real-time Sync:** Trạng thái "Đã đọc" đồng bộ tức thì lên server và các nền tảng khác.

#### 3.4 Xử lý Đánh dấu tất cả đã đọc (Bổ sung)
1. Người dùng tap "Đánh dấu tất cả đã đọc" (Icon tick đôi ✓✓).
   - **Icon ✓✓ luôn hiển thị và enabled** — không bị disable khi không có thông báo chưa đọc.
2. Hệ thống gọi API batch-update đánh dấu tất cả thông báo trong tab hiện tại là đã đọc.
3. **UI optimistic update:** Ngay khi API gọi thành công → Xóa chấm đỏ, badge trên icon chuông cập nhật lại số lượng chính xác.
4. **Rollback on failure:** Nếu API batch-update thất bại → Client rollback UI (khôi phục lại chấm đỏ và style bold ban đầu), hiển thị toast lỗi: *"Không thể đánh dấu tất cả. Vui lòng thử lại."*

#### 3.5 Phân biệt thông báo Cá nhân vs Tổ chức

| Loại tài khoản | Loại thông báo nhận được |
|---|---|
| **Cá nhân** | Thông báo liên quan đến hồ sơ cá nhân, báo cáo cá nhân, thông tin cá nhân khác |
| **Tổ chức** | Thông báo liên quan đến dự án đầu tư, báo cáo doanh nghiệp, nghĩa vụ tài chính công ty, điều chỉnh/gia hạn dự án |

- Loại thông báo "Nhắc hạn" có thể khác nhau giữa 2 loại tài khoản (xem bảng mapping §2.4)

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Giao diện khớp mockup về màu sắc tag màu theo loại thông báo (Blue/Orange/Grey/Red).
- **AC2:** Deep link phải điều hướng chính xác đến UC46 cho các thông báo liên quan đến hồ sơ.
- **AC3:** Thời gian hiển thị In-app banner phải đạt đúng **3 giây**.
- **AC4:** Tính năng "Đánh dấu tất cả" phải cập nhật trạng thái đồng bộ cho toàn bộ tab hiện tại.

---

## 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-08 | v2 -> v3 | Toàn bộ tài liệu | Tài liệu v2 | Tài liệu v3 tích hợp nội dung bổ sung | Hợp nhất chi tiết từ file BoSung |
| 2026-05-08 | v2 -> v3 | Mục 2.3, 2.4, 2.5 | (Không có) | Thêm phân loại, Cài đặt và Deep link | Bổ sung theo yêu cầu nghiệp vụ chi tiết |
| 2026-05-08 | v2 -> v3 | Mục 3.2.1 | Hiện Banner trong 3 giây | Hiện Banner trong 4 giây | Cập nhật thời gian hiển thị banner |
| 2026-05-08 | v2 -> v3 | Mục 3.4 | (Không có) | Xử lý Đánh dấu tất cả đã đọc | Bổ sung logic xử lý theo lô |
| 2026-05-13 | v3 -> v4 | Toàn bộ feedback Q1-Q29 | (Nhiều mục) | (a) §3.1: sort 2-tier, số ngày còn lại, empty state CMR-14, error/loading CMR-07/16, pull-to-refresh CMR-13; (b) §3.2: push timing 3s, banner tap/dismiss/stacking, app killed push, new notification auto-appear; (c) §2.2: loại bỏ màn chi tiết; (d) §2.3: badge→tag màu; (e) §2.4: navigation path, toggle scope, auto-save, OS permission denied; (f) §2.5: deep link mapping 6 loại nhắc hạn + 404 handling; (g) §3.5: Org vs Individual notification | Theo Feedback Answers v1 |
| 2026-05-13 | v4 -> v5 | Đổi tên UC: UC258-259 → UC229-243 | UC258 & UC259 | UC229-243 | Đổi tên theo yêu cầu |
| 2026-05-13 | v5 -> v6 | Xóa §2.4 Cài đặt thông báo (thuộc UC260, đã chuyển sang UC254-258-259-260) | Còn §2.4 Cài đặt thông báo | Đã xóa, §2.4 trở thành Deep Link | Tách nhóm E.I (UC254-260) khỏi nhóm E.II (UC229-243) |
